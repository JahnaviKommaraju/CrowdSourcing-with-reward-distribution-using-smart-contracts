// SPDX-License-Identifier: MIT
pragma solidity >=0.4.25 <0.9.0;
pragma experimental ABIEncoderV2;

contract CrowdSource{

    struct Worker{
        uint totalsubmittedReports;
        uint TotalAvgRating;
        uint[] allSubmittedReportIds;
    }
    struct Task{
        string taskTitle;
        string taskDescription;
        address taskCreatorAddress;
        uint minAmt;

    }
    struct Report{
         string reportName;
        string reportContent;
        address ReportCreatorAddress;
        uint avgRating;
        uint totalReviews;
        address[] workers;
    }
    struct WorkerReview{
        uint rating;
        string comments;
        bool IsReportReviewedByWorker;
    }

    Worker newWorker;
    Task newTask;
    Report newReport;
    WorkerReview newReview;
    uint public TotalTasks;
    uint public TotalReports;
    uint public TotalRating;
    uint public TotalwSubmittedReports;

    mapping(uint=>Task) taskDetails;
    uint[] public TaskIds;
    mapping(uint => Report) reportDetails;
    uint[] public ReportIds;
    mapping(uint => mapping(address =>WorkerReview)) workerReviewDetails;

    mapping(address => Worker) workerDetails;
    uint[] public rIdSubmittedByWorkerAddress;

    event addTaskEvent(uint tid, string tName);
    event addReportEvent(uint rid, string rname);
    event reviewReportEvent(uint rid, uint avgRating);

    constructor(){
       TotalTasks=0; 
       TotalReports = 0;
       TotalRating=0;
       TotalwSubmittedReports=0;
    }

    function addTask(address rAddress,string memory tName, string memory tDescription, uint minAmtForTask) public{
        require(keccak256(bytes(tDescription)) != keccak256(""),"Task Description required !");
        TotalTasks++;
        uint tid = TotalTasks + 110; 
        newTask.taskTitle = tName;
        newTask.taskDescription = tDescription;
        newTask.minAmt = minAmtForTask;
        newTask.taskCreatorAddress= rAddress;
        TaskIds.push(tid);
        taskDetails[tid] = newTask;

        emit addTaskEvent(TotalTasks, tName);

    }

    function getTotalTasks() public view returns(uint){
        return TotalTasks;
    }

    function getTask(uint tid) public view returns(Task memory){
        return taskDetails[tid];
    }

    function getAllTaskIds() public view returns (uint[] memory) {
        return TaskIds;
    }

    function addReport(address wAddress,string memory rname,string memory _content) public{
        require(keccak256(bytes(_content)) != keccak256(""),"Report content required !");
        TotalReports++;
        uint rid = TotalReports+ 111110;

        newReport.reportName = rname;
        newReport.reportContent= _content;
        newReport.avgRating= 0;
        newReport.totalReviews=0;
        newReport.workers.push(wAddress);
        newReport.ReportCreatorAddress=wAddress;
        ReportIds.push(rid);
        reportDetails[rid] = newReport; 

        newWorker.totalsubmittedReports= TotalwSubmittedReports+1;
        rIdSubmittedByWorkerAddress.push(rid);
        workerDetails[wAddress]=newWorker;

        emit addReportEvent(TotalReports,rname);
    }

   
    function getTotalReports() public view returns(uint){
        return TotalReports;
    }

    function getReport(uint rid) public view returns(Report memory){
        return reportDetails[rid];
    }

    function getAllReportIds() public view returns (uint[] memory) {
        return ReportIds;
    }

    function getReportsSubmittedByWorker() public view returns(uint[] memory){
        return rIdSubmittedByWorkerAddress;
    }
    function reviewReport(address wAddress, uint reportId, uint wRating,string memory wComments) public{
        require(reportId>=0,"Report id required!");
        require(wRating>0 && wRating<=5, "Report rating should be in 1-5 range!");
        require(workerReviewDetails[reportId][msg.sender].IsReportReviewedByWorker==false,"Report already reviewed by this worker!");

        Report storage oldReport = reportDetails[reportId];
        oldReport.avgRating+=wRating*10;
        oldReport.totalReviews++;
        oldReport.workers.push(wAddress);

        newReview.rating = wRating;
        newReview.comments = wComments;
        newReview.IsReportReviewedByWorker = true;

        workerReviewDetails[reportId][wAddress] = newReview;

        emit reviewReportEvent(reportId,wRating);
    }

    function getReportAvgRating(uint rid) public view returns(string memory rname,uint avgrating){
        require(rid>=0,"Reportid required!");
        
        uint allAvgRating =0;
        if(reportDetails[rid].totalReviews>0){
            allAvgRating= reportDetails[rid].avgRating/ reportDetails[rid].totalReviews;
        }
        return (reportDetails[rid].reportName, allAvgRating);
    }

    function getCurrentWorkerComments(uint rid) public view returns(string memory wComments){
        require(rid>=0, "Reportid required");

        return workerReviewDetails[rid][msg.sender].comments;
    }

    function getCurrentWorkerRating(uint rid) public view returns(uint wRating){
        require(rid>=0, "Reportid required");

        return workerReviewDetails[rid][msg.sender].rating;
    }

    function getWorkerComments(uint rid, address worker) public view returns(string memory wComments){
         require(rid>=0, "Reportid required");
         return workerReviewDetails[rid][worker].comments;
    }

    function getWorkerRating(uint rid, address worker) public view returns(uint wRating){
         require(rid>=0, "Reportid required");
         return workerReviewDetails[rid][worker].rating;
    }

    function getAllWorkersForReport(uint rid) public view returns(address[] memory){
        return reportDetails[rid].workers;
    }


}   