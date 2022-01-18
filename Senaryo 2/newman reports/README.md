# Newman Raporlama

Newman raporlarıma ulaşmak için klasörde bulunan html dosyasını indirip herhangi bir browser ile açmanız yeterli olacaktır.



```html
<!DOCTYPE html>
<html lang="en" style="overflow-y: scroll;">
<head>
  <meta charset="UTF-8">
  <title>Newman Summary Report</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/styles/default.min.css">
  <link rel="stylesheet" href="https://cdn.datatables.net/v/bs4/dt-1.10.18/datatables.min.css"/>

<style>
code.renderMarkdown table, code.renderMarkdown th, code.renderMarkdown td {
    border: 1px solid black;
    width: max-content;
    padding: .75rem;
}

.theme-dark {
    --background-color: #222;
    --bg-card-deck: #444444;
    --text-color: #ccd2d8;
    --tab-border: solid 1px #444;
    --success: #3c9372;
    --failure: #c24a3f;
    --warning: #d28c23;
    --info: #4083b6;
    --badge-outline: #3c9372;
    --badge-bg: #cdd3db;
    --badge-text: #ccd2d9;
    --failure-row: #c24a3f;
    --warning-row: #d28c23;
    --card-bg: #444;
    --card-footer: #4f5758;
    --form-input: #ececb5;
    --hov-text: #d2dae5;
    --h4-text: #ccd1d9;
}

.theme-light {
    --tab-border: solid 1px #fff;
    --text-color: #000000;
    --success: #42a745;
    --failure: #dc3544;
    --warning: #f4c10b;
    --info: #49a1b8;
    --badge-outline: #040411;
    --badge-bg: #f8f9fa;
    --badge-text: #fff;
    --failure-row: #f5c6cb;
    --warning-row: #ffeeba;
    --card-bg: #f7f7f7;
    --hov-text: #fff;
    --h4-text: #ffffff;
}

body {
  padding-top:30px;
  background-color: var(--background-color)!important;
  color: var(--text-color);
}

#execution-data {
  padding: 10px;
  border: var(--tab-border);
  border-top: none;
}

.nav-tabs {
  padding-top: 10px;
  height: 105px;
  overflow-y: auto;
}

body.theme-dark .card-header {
    background-color: #444;
}

body.theme-light .card-header {
    background-color: #f7f7f7;
}

.card-footer {
    padding: .75rem 1.25rem;
    background-color: var(--card-footer);
}

.card-deck {
    background-color: var(--bg-card-deck)!important;
}
.form-control {
    background: var(--form-input);
}

.custom-tab {
  padding: 10px 15px;
  margin-right: 0px;
  height: 47px;
  width: 69px;
  text-align: center;
  border: var(--tab-border);
  border-bottom: none;
  cursor:pointer;
}

body.theme-dark .text-white {
    color: #ccd2d9!important;
}
h4 {
    color: var(--h4-text);
}

body.theme-dark h1 {
    color: #ccd2da;
}

body.theme-dark .bg-light>td {
    background: #4f5858!important;
}

body.theme-dark .hljs {
    background: #0a0a0ab0!important;
    color: #8d8787!important;
}

.bg-info {
    background-color: var(--info)!important;
}
.bg-success {
    background-color: var(--success)!important;
}

.alert-success {
    background-color: var(--success)!important;
}

.alert-warning {
    background-color: var(--warning)!important;
}

.alert-info {
    background-color: var(--info)!important;
}

.bg-warning {
    background-color: var(--warning)!important;
}

.badge-warning {
    color: var(--badge-text)!important;
    background-color: var(--warning)!important;
}

.table-warning>td {
    background-color: var(--warning-row);
}

.alert-danger {
    background-color: var(--failure)!important;
}

body.theme-dark .alert-dark {
    background-color: #636467!important;
}

body.theme-dark .text-dark {
    color: #d1dae4!important;
}

body.theme-dark .badge-light {
    color: #212529;
    background-color: #cdd3db;
}

body.theme-light .badge-light {
    color: #212529;
    background-color: #f8f9fa;
}
body.theme-light .bg-danger {
    background-color: var(--failure)!important;
}

body.theme-dark .bg-danger {
    background-color: var(--failure)!important;
}

.table-danger>td {
    background-color: var(--failure-row);
}

body.theme-dark .table .thead-light th {
    background-color: #4f5858!important;
    border-color: #dee2e6!important;
    color: #ccd2d8!important;
}

.itPassed {
  background: var(--success);
  color: white;
}
.itFailed {
  background: var(--failure);
  color: white;
}

.resultsInfoPass {
  color: var(--success);
  padding-top: 4px;
}

.resultsInfoFail {
  color: var(--failure);
  padding-top: 4px;
}

.badge-outline-success {
  color: var(--success);
  border: 1px solid var(--success);
  background-color: transparent;
}

.badge-outline {
  color: var(--badge-outline);
  border: 1px solid var(--badge-outline);
  background-color: transparent;
}

.btn-outline-success {
    color: var(--success)!important;
    border-color: var(--success)!important;
}

.backToTop:hover {
  background-color: var(--success);
  border-color: var(--success);
  color: var(--hov-text)!important;
}

.btn-outline-success:hover {
  background-color: var(--success);
  border-color: var(--success);
  color: var(--hov-text)!important;
}

.btn-outline-secondary {
  background-color: var(--success)!important;
  color: var(--hov-text)!important;
}

body.theme-dark .env-heading {
    color: #ccd2d9!important;
}

body, html {
  height:100%;
}

.card {
  overflow:hidden;
}

body.theme-dark .card-body {
    background-color: #444;
}

body.theme-light .card-body {
    background-color: #f7f7f7;
}

body.theme-dark .card-body .bg-danger {
    background-color: var(--failure)!important;
}

body.theme-light .card-body .bg-danger {
    background-color: var(--failure)!important;
}

.card-body .rotate {
  z-index: 8;
  float: right;
  height: 100%;
}

.card-body .rotate i {
  color: #14141426;
  position: absolute;
  left: 0;
  left: auto;
  right: -10px;
  bottom: 0;
  display: block;
  -webkit-transform: rotate(-44deg);
  -moz-transform: rotate(-44deg);
  -o-transform: rotate(-44deg);
  -ms-transform: rotate(-44deg);
  transform: rotate(-44deg);
}

.dyn-height {
  max-height:350px;
  overflow-y:auto;
}

.nav-pills .nav-link.active {
  background-color: transparent!important;
}

.backToTop {
  display: none;
  position: fixed;
  bottom: 10px;
  right: 20px;
  z-index: 99;
  font-size: 15px;
  outline: none;
  cursor: pointer;
  padding: 15px;
  border-radius: 4px;
}

.card-header .fa {
  transition: .3s transform ease-in-out;
}
.card-header .collapsed .fa {
  transform: rotate(90deg);
}

.single-line-tabs {
  padding-top: 10px;
  height: 60px;
}

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1; 
}

::-webkit-scrollbar-thumb {
  background: #888; 
}

::-webkit-scrollbar-thumb:hover {
  background: #555; 
}

/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 20px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 20px;
  width: 20px;
  left: 0px;
  bottom: 4px;
  top: 0;
  bottom: 0;
  margin: auto 0;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  box-shadow: 0 0px 15px #2020203d;
  background: white;
  background-repeat: no-repeat;
  background-position: center;
}

input:checked + .slider {
  background-color: #4083b6;
}

input:focus + .slider {
  box-shadow: 0 0 1px #4083b6;
}

input:checked + .slider:before {
  -webkit-transform: translateX(24px);
  -ms-transform: translateX(24px);
  transform: translateX(24px);
  background: white;
  background-repeat: no-repeat;
  background-position: center;
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}

table.dataTable td, table.dataTable tr {
    vertical-align: middle;
} 

body.theme-dark code {
    color: #ccd2d8!important;
} 

body.theme-light code {
    color: #000000!important;
} 

</style>
</head>
<body class="">
  <div class="container">
        <div class="container">
            <label>Light</label>
            <label id="switch" class="switch">
                <input type="checkbox" onchange="toggleTheme()" id="slider">
                <span class="slider round"></span>
            </label>
            <label>Dark</label>
        </div>
        <div class="card">
        <div class="card-header">
            <ul class="nav nav-pills mb-3 nav-justified" id="pills-tab" role="tablist">
            <li class="nav-item bg-info active" data-toggle="tooltip" title="Click to view the Summary">
                <a class="nav-link text-white" id="pills-summary-tab" data-toggle="pill" href="#pills-summary" role="tab" aria-controls="pills-summary" aria-selected="true">Summary</a>
            </li>
            <li class="nav-item bg-success" data-toggle="tooltip" title="Click to view the Requests">
                <a class="nav-link text-white" id="pills-requests-tab" data-toggle="pill" href="#pills-requests" role="tab" aria-controls="pills-requests" aria-selected="false">Total Requests <span class="badge badge-light">8</span></a>
            </li>
            <li class="nav-item bg-danger" data-toggle="tooltip" title="Click to view the Failed Tests">
                <a class="nav-link text-white" id="pills-failed-tab" data-toggle="pill" href="#pills-failed" role="tab" aria-controls="pills-failed" aria-selected="false">Failed Tests <span class="badge badge-light">2</span></a>
            </li>
            <li class="nav-item bg-warning" data-toggle="tooltip" title="Click to view the Skipped Tests">
                <a class="nav-link text-white" id="pills-skipped-tab" data-toggle="pill" href="#pills-skipped" role="tab" aria-controls="pills-skipped" aria-selected="false">Skipped Tests <span class="badge badge-light">0</span></a>
            </li>
            </ul>
        <div class="tab-content" id="pills-tabContent">
            <div class="tab-pane fade show active" id="pills-summary" role="tabcard" aria-labelledby="pills-summary-tab">
<div class="row">
  <div class="col-md-9 col-lg-12 main">
   <h1 class="display-2 text-center">Newman Run Dashboard</h1>
   <h5 class="text-center">Tuesday, 18 January 2022 15:17:31</h5>
   <div class="row">
    <div class="col-lg-3 col-md-6">
     <div class="card text-white card-success">
      <div class="card-body bg-danger">
       <div class="rotate">
        <i class="fa fa-retweet fa-5x"></i>
       </div>
       <h6 class="text-uppercase">Total Iterations</h6>
       <h1 class="display-1">1</h1>
      </div>
     </div>
    </div>
    <div class="col-lg-3 col-md-6">
     <div class="card text-white card-danger">
      <div class="card-body bg-success">
       <div class="rotate">
        <i class="fa fa-list fa-4x"></i>
       </div>
       <h6 class="text-uppercase">Total Assertions</h6>
       <h1 class="display-1">31</h1>
      </div>
     </div>
    </div>
    <div class="col-lg-3 col-md-6">
     <div class="card text-white card-info">
      <div class="card-body bg-danger">
       <div class="rotate">
        <i class="fa fa-plus-circle fa-5x"></i>
       </div>
       <h6 class="text-uppercase">Total Failed Tests</h6>
       <h1 class="display-1">2</h1>
      </div>
     </div>
    </div>
    <div class="col-lg-3 col-md-6">
     <div class="card text-white card-warning">
      <div class="card-body bg-success">
       <div class="rotate">
        <i class="fa fa-share fa-5x"></i>
       </div>
       <h6 class="text-uppercase">Total Skipped Tests</h6>
       <h1 class="display-1">0</h1>
      </div>
     </div>
    </div>
   </div>
   <hr>
    <div class="row">
    <div class="col">
        <div class="row">
        <div class="col-sm-12 mb-3">
            <div class="card border-info">
                <div class="card-body">
                <h5 class="card-title text-uppercase text-white text-center bg-info">File Information</h5>
                <span><i class="fas fa-file-code"></i></span><strong> Collection:</strong> Test Automation Bootcamp API<br>
                
                <span><i class="fas fa-file-code"></i></span><strong> Environment:</strong> CicekSepetiBitirmeENV<br>
                </div>
            </div>
        </div>
        </div>
        <div class="row">
        <div class="col-sm-12 mb-3">
            <div class="card border-info">
                <div class="card-body">
                <h5 class="card-title text-uppercase text-white text-center bg-info">Timings and Data</h5>
                <span><i class="fas fa-stopwatch"></i></span><strong> Total run duration:</strong> 2s<br>
                <span><i class="fas fa-database"></i></span><strong> Total data received:</strong> 1.13KB<br>
                <span><i class="fas fa-stopwatch"></i></span><strong> Average response time:</strong> 162ms<br>
                </div>
            </div>
        </div>
        </div>
        <div class="row">
        <div class="col-sm-12 mb-3">
            <div class="table-responsive">
            <table class="table table-striped table-bordered">
                <thead class="thead-inverse">
                    <tr class="text-center">
                        <th class="text-uppercase">Summary Item</th>
                        <th class="text-uppercase">Total</th>
                        <th class="text-uppercase">Failed</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Requests</td>
                        <td class="text-center">8</td>
                        <td class="text-center">0</td>
                    </tr>
                    <tr>
                        <td>Prerequest Scripts</td>
                        <td class="text-center">8</td>
                        <td class="text-center">0</td>
                    </tr>
                    <tr>
                        <td>Test Scripts</td>
                        <td class="text-center">8</td>
                        <td class="text-center">0</td>
                    </tr>
                    <tr class="table-danger">
                        <td>Assertions</td>
                        <td class="text-center">31</td>
                        <td class="text-center">2</td>
                    </tr>
                    <tr class="">
                        <td>Skipped Tests</td>
                        <td class="text-center">0</td>
                        <td class="text-center">-</td>
                    </tr>
                </tbody>
            </table>
            </div>
        </div>
        </div>
    <hr>
   </div>
   </div>
  </div>
 </div>
        </div>
            <div class="tab-pane fade" id="pills-failed" role="tabcard" aria-labelledby="pills-failed-tab">
                <button id="topOfFailuresScreen" class="btn btn-outline-success btn-sm backToTop" onclick="topFunction()">Go To Top</button>
                
                    <div class="btn-group float-right" role="group" aria-label="Button Group">
                        <button id="openAllFailed" class="btn btn-outline-success btn-sm float-right" style="text-align: center; width: 185px;">Expand All Failed Tests</button>
                    </div>
                    <br>
                    <br>

                    <div class="alert alert-danger text-uppercase text-center">
                        <h4>Showing 2 Failures</h4>
                    </div>
                    <div class="col-sm-12 mb-3">
                    <div class="card-deck">
                        <div class="card border-danger">
                            <div class="card-header bg-danger">
                                <a data-toggle="collapse" href="#" data-target="#fails-collapse-c657f7d8-6085-43f2-b982-fad4f04c4eee" aria-expanded="false" aria-controls="collapse" id="fails-c657f7d8-6085-43f2-b982-fad4f04c4eee" class="collapsed text-white z-block">
                                    Iteration 1 - AssertionError - Test Automation Bootcamp API - Sign Up Success <i class="float-lg-right fa fa-chevron-down" style="padding-top:5px;"></i>
                                </a>
                            </div>
                            <div id="fails-collapse-c657f7d8-6085-43f2-b982-fad4f04c4eee" class="collapse" aria-labelledby="fails-c657f7d8-6085-43f2-b982-fad4f04c4eee">
                            <div class="card-body">
                                <h5 ><strong>Failed Test:</strong> Status code is 200</h5>
                            <hr>
                            <h5 class="card-title text-uppercase text-white text-center bg-danger">Assertion Error Message</h5>
                            <div>
                                <pre><code >Status received is 201. User successfully signed-up -&gt; Response code must be 200 due to Swagger API Documentation. : expected 201 to equal 200</code></pre>
                            </div>
                            </div>
                            </div>
                        </div>
                    </div>
                    </div>
                    <div class="col-sm-12 mb-3">
                    <div class="card-deck">
                        <div class="card border-danger">
                            <div class="card-header bg-danger">
                                <a data-toggle="collapse" href="#" data-target="#fails-collapse-6cdb60b5-a078-44af-a198-e8ec4344ba1c" aria-expanded="false" aria-controls="collapse" id="fails-6cdb60b5-a078-44af-a198-e8ec4344ba1c" class="collapsed text-white z-block">
                                    Iteration 1 - AssertionError - Test Automation Bootcamp API - Sign In Success <i class="float-lg-right fa fa-chevron-down" style="padding-top:5px;"></i>
                                </a>
                            </div>
                            <div id="fails-collapse-6cdb60b5-a078-44af-a198-e8ec4344ba1c" class="collapse" aria-labelledby="fails-6cdb60b5-a078-44af-a198-e8ec4344ba1c">
                            <div class="card-body">
                                <h5 ><strong>Failed Test:</strong> Status Code is 200</h5>
                            <hr>
                            <h5 class="card-title text-uppercase text-white text-center bg-danger">Assertion Error Message</h5>
                            <div>
                                <pre><code >Status received is 201. User successfully signed-up -&gt; Response code must be 200 due to Swagger API Documentation. : expected 201 to equal 200</code></pre>
                            </div>
                            </div>
                            </div>
                        </div>
                    </div>
                    </div>
            </div>

            <div class="tab-pane fade" id="pills-skipped" role="tabcard" aria-labelledby="pills-skipped-tab">
                <button id="topOfSkippedScreen" class="btn btn-outline-success btn-sm backToTop" onclick="topFunction()">Go To Top</button>

                <div class="alert alert-success text-uppercase text-center">
                    <br><br><h1 class="text-center">There are no skipped tests <span><i class="far fa-thumbs-up"></i></span></h1><br><br>
                </div>
            </div>
            <div class="tab-pane fade" id="pills-requests" role="tabcard" aria-labelledby="pills-requests-tab">

            <button id="topOfRequestsScreen" class="btn btn-outline-success btn-sm backToTop" onclick="topFunction()">Go To Top</button>
            
            <div class="btn-group float-right" role="group" aria-label="Button Group">
                <button id="showOnlyFailures" class="btn btn-outline-success btn-sm float-right" style="text-align: center; width:160px;">Show Failed Iterations</button>
                <button id="openAll" class="btn btn-outline-success btn-sm float-right" style="text-align: center; width: 140px;">Expand Folders</button>
                <button id="openAllRequests" class="btn btn-outline-success btn-sm float-right" style="text-align: center; width: 140px;">Expand Requests</button>
            </div>

    <div class="text-uppercase" id="execution-menu">
        <h5>1 Iteration available to view</h5>
        
        <nav class="table-responsive">
        <ul class="nav single-line-tabs" id="iterationList">
        </ul>
        </nav>
    </div>
    <h6 class="text-uppercase text-muted" id="iterationSelected" style="padding-top: 10px;"></h6>
	<div class="tab-content" id="execution-data">
            <div id="folder-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a" class="card-deck iteration-0">
            <div class="row iteration-0">
                <div class="col-sm-12 mb-3 iteration-0">
                <div class="card iteration-0">
                    <div class="card-header  bg-danger iteration-0">
                        <a data-toggle="collapse" href="#" data-target="#collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a" aria-expanded="false" aria-controls="collapse" id="requests-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a" class="collapsed text-white z-block">
                    Iteration: 1 - Sign Up Success <i class="float-lg-right fa fa-chevron-down" style="padding-top: 5px;"></i>
                </a>
                    </div>
                    <div id="collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a" class="collapse" aria-labelledby="requests-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request Method:</strong> <span class="badge-outline-success badge badge-success"> POST</span><br>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request URL:</strong> <a href="https://bootcampapi.techcs.io/api/fe/v1/authorization/signup" target="_blank">https://bootcampapi.techcs.io/api/fe/v1/authorization/signup</a><br>
                                    </div>
                                </div>
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Response Code:</strong> <span class="float-right badge-outline badge badge-success"> 201 - Created</span><br>
                                    <span><i class="fas fa-stopwatch"></i></span><strong> Mean time per request:</strong> <span class="float-right badge-outline badge badge-success"> 594ms</span><br>
                                    <span><i class="fas fa-database"></i></span><strong> Mean size per request:</strong> <span class="float-right badge-outline badge badge-success"> 194B</span><br>
                                    <hr>
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Test Pass Percentage</h5>
                                    <div>
                                        <div class="progress" style="height: 40px;">
                                            <div class="progress-bar  bg-danger" style="width: 100%" role="progressbar">
                                            <h5 style="padding-top:5px;"><strong>67 %</strong></h5>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                        <h5 class="card-title text-uppercase text-white text-center bg-info">Request Headers</h5>
                                        <div class="table-responsive">
                                            <table class="table table-bordered">
                                            <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Type</td>
                                                        <td>application/json</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">User-Agent</td>
                                                        <td>PostmanRuntime/7.29.0</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept</td>
                                                        <td>*/*</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cache-Control</td>
                                                        <td>no-cache</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Postman-Token</td>
                                                        <td>49c60acc-11c8-486c-971a-f40d6b850b21</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Host</td>
                                                        <td>bootcampapi.techcs.io</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept-Encoding</td>
                                                        <td>gzip, deflate, br</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Connection</td>
                                                        <td>keep-alive</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Length</td>
                                                        <td>59</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Body</h5>
                                        <div class="dyn-height">
                                            <pre><code id="copyReqText-0" class="prettyPrint">{
          &quot;email&quot;: &quot;8qw@4atv7.com&quot;,
          &quot;password&quot;: &quot;n522fdn9&quot;
        }</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyReqText-0">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Headers</h5>
                                    <div class="table-responsive">
                                        <table class="table table-bordered">
                                        <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-nowrap">Content-Type</td>
                                                    <td>application/json; charset&#x3D;utf-8</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Content-Length</td>
                                                    <td>194</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Connection</td>
                                                    <td>keep-alive</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-powered-by</td>
                                                    <td>Express</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">access-control-allow-origin</td>
                                                    <td>*</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">set-cookie</td>
                                                    <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijhxd0A0YXR2Ny5jb20iLCJpZCI6IlpEMnM2OThmT2lKeWFKS0o3c3BOIiwiaWF0IjoxNjQyNTA4MjQ5fQ.iR-olW1R5jE-55yaHVibt6Vu5w7I_FnhKecn4YaSYQM; Path&#x3D;/; HttpOnly</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">etag</td>
                                                    <td>W/&quot;c2-L756F5satqDQ3/K8WudbMC8Y294&quot;</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">date</td>
                                                    <td>Tue, 18 Jan 2022 12:17:29 GMT</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-envoy-upstream-service-time</td>
                                                    <td>222</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">server</td>
                                                    <td>istio-envoy</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Cache</td>
                                                    <td>Miss from cloudfront</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Via</td>
                                                    <td>1.1 a267c4458d5587daaaf85f1d134a02d4.cloudfront.net (CloudFront)</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Pop</td>
                                                    <td>FRA50-C1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Id</td>
                                                    <td>SumT1pNqGuqNZDIymZRzTtWDJSOTPQjWWPJi6f4t0D9Pf0NAW9ibSA&#x3D;&#x3D;</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Body</h5>
                                        <div class="dyn-height">
                                                <pre><code id="copyText-ce3aa8db-1800-462d-88b2-3bd4d965a634" class="prettyPrint">{&quot;access_token&quot;:&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijhxd0A0YXR2Ny5jb20iLCJpZCI6IlpEMnM2OThmT2lKeWFKS0o3c3BOIiwiaWF0IjoxNjQyNTA4MjQ5fQ.iR-olW1R5jE-55yaHVibt6Vu5w7I_FnhKecn4YaSYQM&quot;}</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyText-ce3aa8db-1800-462d-88b2-3bd4d965a634">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="card border-info">
                                <div class="card-body">
                                <h5 class="card-title text-uppercase text-white text-center bg-info">Test Information</h5>
                                    <div class="table-responsive text-nowrap">
                                        <table id="myTable-ce3aa8db-1800-462d-88b2-3bd4d965a634" class="table table-hover">
                                        <thead><tr class="text-center"><th>Name</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead>
                                            <tbody>
                                                <tr >
                                                    <td >Request Body is Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Signed Up Successfully.</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Status code is 200</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center bg-danger">1</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-light">
                                                    <td><strong>Total</strong></td>
                                                    <td class="text-center">2</td>
                                                    <td class="text-center">1</td>
                                                    <td class="text-center">0</td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>
                                    <div class="row ">
                                    <div class="col-sm-12 mb-3">
                                        <div class="card-deck">
                                        <div class="card border-danger" style="width: 50rem;">
                                            <div class="card-body">
                                                <h5 class="card-title text-uppercase text-white text-center bg-danger">Test Failure</h5>
                                                <div class="table-responsive">
                                                    <table class="table table-hover">
                                                    <thead><tr class="text-nowrap"><th>Test Name</th><th>Assertion Error</th></tr></thead>
                                                        <tbody>
                                                            <tr>
                                                                <td class="w-45 text-nowrap ">Status code is 200</td>
                                                                <td class="w-55"><pre><code >Status received is 201. User successfully signed-up -&gt; Response code must be 200 due to Swagger API Documentation. : expected 201 to equal 200</code></pre></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <div id="folder-ec44a978-2098-4b07-9d9f-9673b796b143" class="card-deck iteration-0">
            <div class="row iteration-0">
                <div class="col-sm-12 mb-3 iteration-0">
                <div class="card iteration-0">
                    <div class="card-header  bg-danger iteration-0">
                        <a data-toggle="collapse" href="#" data-target="#collapse-ec44a978-2098-4b07-9d9f-9673b796b143" aria-expanded="false" aria-controls="collapse" id="requests-ec44a978-2098-4b07-9d9f-9673b796b143" class="collapsed text-white z-block">
                    Iteration: 1 - Sign In Success <i class="float-lg-right fa fa-chevron-down" style="padding-top: 5px;"></i>
                </a>
                    </div>
                    <div id="collapse-ec44a978-2098-4b07-9d9f-9673b796b143" class="collapse" aria-labelledby="requests-ec44a978-2098-4b07-9d9f-9673b796b143">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request Method:</strong> <span class="badge-outline-success badge badge-success"> POST</span><br>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request URL:</strong> <a href="https://bootcampapi.techcs.io/api/fe/v1/authorization/signin" target="_blank">https://bootcampapi.techcs.io/api/fe/v1/authorization/signin</a><br>
                                    </div>
                                </div>
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Response Code:</strong> <span class="float-right badge-outline badge badge-success"> 201 - Created</span><br>
                                    <span><i class="fas fa-stopwatch"></i></span><strong> Mean time per request:</strong> <span class="float-right badge-outline badge badge-success"> 159ms</span><br>
                                    <span><i class="fas fa-database"></i></span><strong> Mean size per request:</strong> <span class="float-right badge-outline badge badge-success"> 194B</span><br>
                                    <hr>
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Test Pass Percentage</h5>
                                    <div>
                                        <div class="progress" style="height: 40px;">
                                            <div class="progress-bar  bg-danger" style="width: 100%" role="progressbar">
                                            <h5 style="padding-top:5px;"><strong>75 %</strong></h5>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                        <h5 class="card-title text-uppercase text-white text-center bg-info">Request Headers</h5>
                                        <div class="table-responsive">
                                            <table class="table table-bordered">
                                            <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Type</td>
                                                        <td>application/json</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">User-Agent</td>
                                                        <td>PostmanRuntime/7.29.0</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept</td>
                                                        <td>*/*</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cache-Control</td>
                                                        <td>no-cache</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Postman-Token</td>
                                                        <td>d7d70999-24e3-48c4-bf26-050ff72544af</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Host</td>
                                                        <td>bootcampapi.techcs.io</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept-Encoding</td>
                                                        <td>gzip, deflate, br</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Connection</td>
                                                        <td>keep-alive</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Length</td>
                                                        <td>59</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cookie</td>
                                                        <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijhxd0A0YXR2Ny5jb20iLCJpZCI6IlpEMnM2OThmT2lKeWFKS0o3c3BOIiwiaWF0IjoxNjQyNTA4MjQ5fQ.iR-olW1R5jE-55yaHVibt6Vu5w7I_FnhKecn4YaSYQM</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Body</h5>
                                        <div class="dyn-height">
                                            <pre><code id="copyReqText-1" class="prettyPrint">{
          &quot;email&quot;: &quot;deneme@db.com&quot;,
          &quot;password&quot;: &quot;12345678&quot;
        }</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyReqText-1">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Headers</h5>
                                    <div class="table-responsive">
                                        <table class="table table-bordered">
                                        <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-nowrap">Content-Type</td>
                                                    <td>application/json; charset&#x3D;utf-8</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Content-Length</td>
                                                    <td>194</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Connection</td>
                                                    <td>keep-alive</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-powered-by</td>
                                                    <td>Express</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">access-control-allow-origin</td>
                                                    <td>*</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">set-cookie</td>
                                                    <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRlbmVtZUBkYi5jb20iLCJpZCI6IjVGbVYzOER0QkJUYk9HYkUxZnB3IiwiaWF0IjoxNjQyNTA4MjQ5fQ.dT8YG0UHLNcxwTcyvuMm4lgAzb3WgpAztjaXnpc_nLk; Path&#x3D;/; HttpOnly</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">etag</td>
                                                    <td>W/&quot;c2-wlC8r6qVko+ik2VgRvtf7+vp8KI&quot;</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">date</td>
                                                    <td>Tue, 18 Jan 2022 12:17:29 GMT</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-envoy-upstream-service-time</td>
                                                    <td>84</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">server</td>
                                                    <td>istio-envoy</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Cache</td>
                                                    <td>Miss from cloudfront</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Via</td>
                                                    <td>1.1 a267c4458d5587daaaf85f1d134a02d4.cloudfront.net (CloudFront)</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Pop</td>
                                                    <td>FRA50-C1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Id</td>
                                                    <td>mXOeSjFilabtTg4T729dfOA-B2E8IcMMf4e21zsk9yOzsaTVrVOlLA&#x3D;&#x3D;</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Body</h5>
                                        <div class="dyn-height">
                                                <pre><code id="copyText-72e041c4-4d3a-4d88-8fd1-aef735edaf14" class="prettyPrint">{&quot;access_token&quot;:&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRlbmVtZUBkYi5jb20iLCJpZCI6IjVGbVYzOER0QkJUYk9HYkUxZnB3IiwiaWF0IjoxNjQyNTA4MjQ5fQ.dT8YG0UHLNcxwTcyvuMm4lgAzb3WgpAztjaXnpc_nLk&quot;}</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyText-72e041c4-4d3a-4d88-8fd1-aef735edaf14">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="card border-info">
                                <div class="card-body">
                                <h5 class="card-title text-uppercase text-white text-center bg-info">Test Information</h5>
                                    <div class="table-responsive text-nowrap">
                                        <table id="myTable-72e041c4-4d3a-4d88-8fd1-aef735edaf14" class="table table-hover">
                                        <thead><tr class="text-center"><th>Name</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead>
                                            <tbody>
                                                <tr >
                                                    <td >Request Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Response Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Signed In Successfully</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Status Code is 200</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center bg-danger">1</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-light">
                                                    <td><strong>Total</strong></td>
                                                    <td class="text-center">3</td>
                                                    <td class="text-center">1</td>
                                                    <td class="text-center">0</td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>
                                    <div class="row ">
                                    <div class="col-sm-12 mb-3">
                                        <div class="card-deck">
                                        <div class="card border-danger" style="width: 50rem;">
                                            <div class="card-body">
                                                <h5 class="card-title text-uppercase text-white text-center bg-danger">Test Failure</h5>
                                                <div class="table-responsive">
                                                    <table class="table table-hover">
                                                    <thead><tr class="text-nowrap"><th>Test Name</th><th>Assertion Error</th></tr></thead>
                                                        <tbody>
                                                            <tr>
                                                                <td class="w-45 text-nowrap ">Status Code is 200</td>
                                                                <td class="w-55"><pre><code >Status received is 201. User successfully signed-up -&gt; Response code must be 200 due to Swagger API Documentation. : expected 201 to equal 200</code></pre></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <div id="folder-d3a8c81d-df29-454a-b204-19cc424d5d1c" class="card-deck iteration-0">
            <div class="row iteration-0">
                <div class="col-sm-12 mb-3 iteration-0">
                <div class="card iteration-0">
                    <div class="card-header  bg-success iteration-0">
                        <a data-toggle="collapse" href="#" data-target="#collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c" aria-expanded="false" aria-controls="collapse" id="requests-d3a8c81d-df29-454a-b204-19cc424d5d1c" class="collapsed text-white z-block">
                    Iteration: 1 - Sign In Fail - Wrong Credentials <i class="float-lg-right fa fa-chevron-down" style="padding-top: 5px;"></i>
                </a>
                    </div>
                    <div id="collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c" class="collapse" aria-labelledby="requests-d3a8c81d-df29-454a-b204-19cc424d5d1c">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request Method:</strong> <span class="badge-outline-success badge badge-success"> POST</span><br>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request URL:</strong> <a href="https://bootcampapi.techcs.io/api/fe/v1/authorization/signin" target="_blank">https://bootcampapi.techcs.io/api/fe/v1/authorization/signin</a><br>
                                    </div>
                                </div>
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Response Code:</strong> <span class="float-right badge-outline badge badge-success"> 401 - Unauthorized</span><br>
                                    <span><i class="fas fa-stopwatch"></i></span><strong> Mean time per request:</strong> <span class="float-right badge-outline badge badge-success"> 158ms</span><br>
                                    <span><i class="fas fa-database"></i></span><strong> Mean size per request:</strong> <span class="float-right badge-outline badge badge-success"> 43B</span><br>
                                    <hr>
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Test Pass Percentage</h5>
                                    <div>
                                        <div class="progress" style="height: 40px;">
                                            <div class="progress-bar  bg-success" style="width: 100%" role="progressbar">
                                            <h5 style="padding-top:5px;"><strong>100 %</strong></h5>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                        <h5 class="card-title text-uppercase text-white text-center bg-info">Request Headers</h5>
                                        <div class="table-responsive">
                                            <table class="table table-bordered">
                                            <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Type</td>
                                                        <td>application/json</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">User-Agent</td>
                                                        <td>PostmanRuntime/7.29.0</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept</td>
                                                        <td>*/*</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cache-Control</td>
                                                        <td>no-cache</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Postman-Token</td>
                                                        <td>3eddd585-6335-4f3b-9e26-8384cea397ca</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Host</td>
                                                        <td>bootcampapi.techcs.io</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept-Encoding</td>
                                                        <td>gzip, deflate, br</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Connection</td>
                                                        <td>keep-alive</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Length</td>
                                                        <td>60</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cookie</td>
                                                        <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRlbmVtZUBkYi5jb20iLCJpZCI6IjVGbVYzOER0QkJUYk9HYkUxZnB3IiwiaWF0IjoxNjQyNTA4MjQ5fQ.dT8YG0UHLNcxwTcyvuMm4lgAzb3WgpAztjaXnpc_nLk</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Body</h5>
                                        <div class="dyn-height">
                                            <pre><code id="copyReqText-2" class="prettyPrint">{
          &quot;email&quot;: &quot;wrongMail&quot;,
          &quot;password&quot;: &quot;wrongPassword&quot;
        }</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyReqText-2">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Headers</h5>
                                    <div class="table-responsive">
                                        <table class="table table-bordered">
                                        <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-nowrap">Content-Type</td>
                                                    <td>application/json; charset&#x3D;utf-8</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Content-Length</td>
                                                    <td>43</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Connection</td>
                                                    <td>keep-alive</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-powered-by</td>
                                                    <td>Express</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">access-control-allow-origin</td>
                                                    <td>*</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">etag</td>
                                                    <td>W/&quot;2b-hGShxOkieaAVDloBubJVM+h58D8&quot;</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">date</td>
                                                    <td>Tue, 18 Jan 2022 12:17:30 GMT</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-envoy-upstream-service-time</td>
                                                    <td>95</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">server</td>
                                                    <td>istio-envoy</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Cache</td>
                                                    <td>Error from cloudfront</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Via</td>
                                                    <td>1.1 a267c4458d5587daaaf85f1d134a02d4.cloudfront.net (CloudFront)</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Pop</td>
                                                    <td>FRA50-C1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Id</td>
                                                    <td>ITowIDYERmJ6NA2py2ZSgAJEJTgXLCqKq9QHm1AZHVLZFp6prhh6KA&#x3D;&#x3D;</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Body</h5>
                                        <div class="dyn-height">
                                                <pre><code id="copyText-1fd7a490-feb8-4ca0-a784-86fec75f8367" class="prettyPrint">{&quot;statusCode&quot;:401,&quot;message&quot;:&quot;Unauthorized&quot;}</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyText-1fd7a490-feb8-4ca0-a784-86fec75f8367">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="card border-info">
                                <div class="card-body">
                                <h5 class="card-title text-uppercase text-white text-center bg-info">Test Information</h5>
                                    <div class="table-responsive text-nowrap">
                                        <table id="myTable-1fd7a490-feb8-4ca0-a784-86fec75f8367" class="table table-hover">
                                        <thead><tr class="text-center"><th>Name</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead>
                                            <tbody>
                                                <tr >
                                                    <td >Request Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Response Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Unsuccessful Sign In</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Status Code is 401</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-light">
                                                    <td><strong>Total</strong></td>
                                                    <td class="text-center">4</td>
                                                    <td class="text-center">0</td>
                                                    <td class="text-center">0</td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>
                                    <div class="row d-none">
                                    <div class="col-sm-12 mb-3">
                                        <div class="card-deck">
                                        <div class="card border-danger" style="width: 50rem;">
                                            <div class="card-body">
                                                <h5 class="card-title text-uppercase text-white text-center bg-danger">Test Failure</h5>
                                                <div class="table-responsive">
                                                    <table class="table table-hover">
                                                    <thead><tr class="text-nowrap"><th>Test Name</th><th>Assertion Error</th></tr></thead>
                                                        <tbody>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <div id="folder-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c" class="card-deck iteration-0">
            <div class="row iteration-0">
                <div class="col-sm-12 mb-3 iteration-0">
                <div class="card iteration-0">
                    <div class="card-header  bg-success iteration-0">
                        <a data-toggle="collapse" href="#" data-target="#collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c" aria-expanded="false" aria-controls="collapse" id="requests-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c" class="collapsed text-white z-block">
                    Iteration: 1 - Sign Up Fail - Invalid Fields <i class="float-lg-right fa fa-chevron-down" style="padding-top: 5px;"></i>
                </a>
                    </div>
                    <div id="collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c" class="collapse" aria-labelledby="requests-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request Method:</strong> <span class="badge-outline-success badge badge-success"> POST</span><br>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request URL:</strong> <a href="https://bootcampapi.techcs.io/api/fe/v1/authorization/signup" target="_blank">https://bootcampapi.techcs.io/api/fe/v1/authorization/signup</a><br>
                                    </div>
                                </div>
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Response Code:</strong> <span class="float-right badge-outline badge badge-success"> 400 - Bad Request</span><br>
                                    <span><i class="fas fa-stopwatch"></i></span><strong> Mean time per request:</strong> <span class="float-right badge-outline badge badge-success"> 60ms</span><br>
                                    <span><i class="fas fa-database"></i></span><strong> Mean size per request:</strong> <span class="float-right badge-outline badge badge-success"> 133B</span><br>
                                    <hr>
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Test Pass Percentage</h5>
                                    <div>
                                        <div class="progress" style="height: 40px;">
                                            <div class="progress-bar  bg-success" style="width: 100%" role="progressbar">
                                            <h5 style="padding-top:5px;"><strong>100 %</strong></h5>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                        <h5 class="card-title text-uppercase text-white text-center bg-info">Request Headers</h5>
                                        <div class="table-responsive">
                                            <table class="table table-bordered">
                                            <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Type</td>
                                                        <td>application/json</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">User-Agent</td>
                                                        <td>PostmanRuntime/7.29.0</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept</td>
                                                        <td>*/*</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cache-Control</td>
                                                        <td>no-cache</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Postman-Token</td>
                                                        <td>95ea6f99-f39a-4f88-98c6-c775fe3c8733</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Host</td>
                                                        <td>bootcampapi.techcs.io</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept-Encoding</td>
                                                        <td>gzip, deflate, br</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Connection</td>
                                                        <td>keep-alive</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Length</td>
                                                        <td>54</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cookie</td>
                                                        <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRlbmVtZUBkYi5jb20iLCJpZCI6IjVGbVYzOER0QkJUYk9HYkUxZnB3IiwiaWF0IjoxNjQyNTA4MjQ5fQ.dT8YG0UHLNcxwTcyvuMm4lgAzb3WgpAztjaXnpc_nLk</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Body</h5>
                                        <div class="dyn-height">
                                            <pre><code id="copyReqText-3" class="prettyPrint">{
          &quot;email&quot;: &quot;u73pw7.com&quot;,
          &quot;password&quot;: &quot;4ruveg&quot;
        }</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyReqText-3">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Headers</h5>
                                    <div class="table-responsive">
                                        <table class="table table-bordered">
                                        <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-nowrap">Content-Type</td>
                                                    <td>application/json; charset&#x3D;utf-8</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Content-Length</td>
                                                    <td>133</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Connection</td>
                                                    <td>keep-alive</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-powered-by</td>
                                                    <td>Express</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">access-control-allow-origin</td>
                                                    <td>*</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">etag</td>
                                                    <td>W/&quot;85-lGOXsaD09ymuXCUTFYyhvjG54pQ&quot;</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">date</td>
                                                    <td>Tue, 18 Jan 2022 12:17:30 GMT</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-envoy-upstream-service-time</td>
                                                    <td>1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">server</td>
                                                    <td>istio-envoy</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Cache</td>
                                                    <td>Error from cloudfront</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Via</td>
                                                    <td>1.1 a267c4458d5587daaaf85f1d134a02d4.cloudfront.net (CloudFront)</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Pop</td>
                                                    <td>FRA50-C1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Id</td>
                                                    <td>KgBS72BdSvjxvcmyCPRW7SyiflujlcAGfzErEboP7BZdiy2KPNg4_Q&#x3D;&#x3D;</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Body</h5>
                                        <div class="dyn-height">
                                                <pre><code id="copyText-166254a8-0a70-4478-b928-8f09a0e0c4b2" class="prettyPrint">{&quot;statusCode&quot;:400,&quot;message&quot;:[&quot;email must be an email&quot;,&quot;password must be longer than or equal to 8 characters&quot;],&quot;error&quot;:&quot;Bad Request&quot;}</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyText-166254a8-0a70-4478-b928-8f09a0e0c4b2">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="card border-info">
                                <div class="card-body">
                                <h5 class="card-title text-uppercase text-white text-center bg-info">Test Information</h5>
                                    <div class="table-responsive text-nowrap">
                                        <table id="myTable-166254a8-0a70-4478-b928-8f09a0e0c4b2" class="table table-hover">
                                        <thead><tr class="text-center"><th>Name</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead>
                                            <tbody>
                                                <tr >
                                                    <td >Request Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Response Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Request Body Invalid Field Errors Case: invalidEmail, invalidPassword</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Status Code is 400</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-light">
                                                    <td><strong>Total</strong></td>
                                                    <td class="text-center">4</td>
                                                    <td class="text-center">0</td>
                                                    <td class="text-center">0</td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>
                                    <div class="row d-none">
                                    <div class="col-sm-12 mb-3">
                                        <div class="card-deck">
                                        <div class="card border-danger" style="width: 50rem;">
                                            <div class="card-body">
                                                <h5 class="card-title text-uppercase text-white text-center bg-danger">Test Failure</h5>
                                                <div class="table-responsive">
                                                    <table class="table table-hover">
                                                    <thead><tr class="text-nowrap"><th>Test Name</th><th>Assertion Error</th></tr></thead>
                                                        <tbody>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <div id="folder-6e63495a-be99-4ffb-9510-4dfe84bfe1f6" class="card-deck iteration-0">
            <div class="row iteration-0">
                <div class="col-sm-12 mb-3 iteration-0">
                <div class="card iteration-0">
                    <div class="card-header  bg-success iteration-0">
                        <a data-toggle="collapse" href="#" data-target="#collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6" aria-expanded="false" aria-controls="collapse" id="requests-6e63495a-be99-4ffb-9510-4dfe84bfe1f6" class="collapsed text-white z-block">
                    Iteration: 1 - Sign Up Fail - Invalid Fields <i class="float-lg-right fa fa-chevron-down" style="padding-top: 5px;"></i>
                </a>
                    </div>
                    <div id="collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6" class="collapse" aria-labelledby="requests-6e63495a-be99-4ffb-9510-4dfe84bfe1f6">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request Method:</strong> <span class="badge-outline-success badge badge-success"> POST</span><br>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request URL:</strong> <a href="https://bootcampapi.techcs.io/api/fe/v1/authorization/signup" target="_blank">https://bootcampapi.techcs.io/api/fe/v1/authorization/signup</a><br>
                                    </div>
                                </div>
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Response Code:</strong> <span class="float-right badge-outline badge badge-success"> 400 - Bad Request</span><br>
                                    <span><i class="fas fa-stopwatch"></i></span><strong> Mean time per request:</strong> <span class="float-right badge-outline badge badge-success"> 61ms</span><br>
                                    <span><i class="fas fa-database"></i></span><strong> Mean size per request:</strong> <span class="float-right badge-outline badge badge-success"> 164B</span><br>
                                    <hr>
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Test Pass Percentage</h5>
                                    <div>
                                        <div class="progress" style="height: 40px;">
                                            <div class="progress-bar  bg-success" style="width: 100%" role="progressbar">
                                            <h5 style="padding-top:5px;"><strong>100 %</strong></h5>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                        <h5 class="card-title text-uppercase text-white text-center bg-info">Request Headers</h5>
                                        <div class="table-responsive">
                                            <table class="table table-bordered">
                                            <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Type</td>
                                                        <td>application/json</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">User-Agent</td>
                                                        <td>PostmanRuntime/7.29.0</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept</td>
                                                        <td>*/*</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cache-Control</td>
                                                        <td>no-cache</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Postman-Token</td>
                                                        <td>c7111b2e-629d-4221-b36d-c62d4e1422b1</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Host</td>
                                                        <td>bootcampapi.techcs.io</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept-Encoding</td>
                                                        <td>gzip, deflate, br</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Connection</td>
                                                        <td>keep-alive</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Length</td>
                                                        <td>48</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cookie</td>
                                                        <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRlbmVtZUBkYi5jb20iLCJpZCI6IjVGbVYzOER0QkJUYk9HYkUxZnB3IiwiaWF0IjoxNjQyNTA4MjQ5fQ.dT8YG0UHLNcxwTcyvuMm4lgAzb3WgpAztjaXnpc_nLk</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Body</h5>
                                        <div class="dyn-height">
                                            <pre><code id="copyReqText-4" class="prettyPrint">{
          &quot;email&quot;: &quot;qerc6p.com&quot;,
          &quot;password&quot;: &quot;&quot;
        }</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyReqText-4">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Headers</h5>
                                    <div class="table-responsive">
                                        <table class="table table-bordered">
                                        <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-nowrap">Content-Type</td>
                                                    <td>application/json; charset&#x3D;utf-8</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Content-Length</td>
                                                    <td>164</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Connection</td>
                                                    <td>keep-alive</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-powered-by</td>
                                                    <td>Express</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">access-control-allow-origin</td>
                                                    <td>*</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">etag</td>
                                                    <td>W/&quot;a4-iOVQ/19cHA/4orvICYGWnZ/sLB4&quot;</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">date</td>
                                                    <td>Tue, 18 Jan 2022 12:17:30 GMT</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-envoy-upstream-service-time</td>
                                                    <td>1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">server</td>
                                                    <td>istio-envoy</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Cache</td>
                                                    <td>Error from cloudfront</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Via</td>
                                                    <td>1.1 a267c4458d5587daaaf85f1d134a02d4.cloudfront.net (CloudFront)</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Pop</td>
                                                    <td>FRA50-C1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Id</td>
                                                    <td>8XbQ5rZHFXCw5x3tSjnfclnWca--FPN9VMpbpbQvXOrqp48Ze19u-w&#x3D;&#x3D;</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Body</h5>
                                        <div class="dyn-height">
                                                <pre><code id="copyText-166254a8-0a70-4478-b928-8f09a0e0c4b2" class="prettyPrint">{&quot;statusCode&quot;:400,&quot;message&quot;:[&quot;email must be an email&quot;,&quot;password must be longer than or equal to 8 characters&quot;,&quot;password should not be empty&quot;],&quot;error&quot;:&quot;Bad Request&quot;}</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyText-166254a8-0a70-4478-b928-8f09a0e0c4b2">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="card border-info">
                                <div class="card-body">
                                <h5 class="card-title text-uppercase text-white text-center bg-info">Test Information</h5>
                                    <div class="table-responsive text-nowrap">
                                        <table id="myTable-166254a8-0a70-4478-b928-8f09a0e0c4b2" class="table table-hover">
                                        <thead><tr class="text-center"><th>Name</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead>
                                            <tbody>
                                                <tr >
                                                    <td >Request Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Response Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Request Body Invalid Field Errors Case: invalidEmail, emptyPassword</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Status Code is 400</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-light">
                                                    <td><strong>Total</strong></td>
                                                    <td class="text-center">4</td>
                                                    <td class="text-center">0</td>
                                                    <td class="text-center">0</td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>
                                    <div class="row d-none">
                                    <div class="col-sm-12 mb-3">
                                        <div class="card-deck">
                                        <div class="card border-danger" style="width: 50rem;">
                                            <div class="card-body">
                                                <h5 class="card-title text-uppercase text-white text-center bg-danger">Test Failure</h5>
                                                <div class="table-responsive">
                                                    <table class="table table-hover">
                                                    <thead><tr class="text-nowrap"><th>Test Name</th><th>Assertion Error</th></tr></thead>
                                                        <tbody>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <div id="folder-0349d8d7-9111-4d8b-836e-998cfc8312a3" class="card-deck iteration-0">
            <div class="row iteration-0">
                <div class="col-sm-12 mb-3 iteration-0">
                <div class="card iteration-0">
                    <div class="card-header  bg-success iteration-0">
                        <a data-toggle="collapse" href="#" data-target="#collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3" aria-expanded="false" aria-controls="collapse" id="requests-0349d8d7-9111-4d8b-836e-998cfc8312a3" class="collapsed text-white z-block">
                    Iteration: 1 - Sign Up Fail - Invalid Fields <i class="float-lg-right fa fa-chevron-down" style="padding-top: 5px;"></i>
                </a>
                    </div>
                    <div id="collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3" class="collapse" aria-labelledby="requests-0349d8d7-9111-4d8b-836e-998cfc8312a3">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request Method:</strong> <span class="badge-outline-success badge badge-success"> POST</span><br>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request URL:</strong> <a href="https://bootcampapi.techcs.io/api/fe/v1/authorization/signup" target="_blank">https://bootcampapi.techcs.io/api/fe/v1/authorization/signup</a><br>
                                    </div>
                                </div>
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Response Code:</strong> <span class="float-right badge-outline badge badge-success"> 400 - Bad Request</span><br>
                                    <span><i class="fas fa-stopwatch"></i></span><strong> Mean time per request:</strong> <span class="float-right badge-outline badge badge-success"> 62ms</span><br>
                                    <span><i class="fas fa-database"></i></span><strong> Mean size per request:</strong> <span class="float-right badge-outline badge badge-success"> 163B</span><br>
                                    <hr>
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Test Pass Percentage</h5>
                                    <div>
                                        <div class="progress" style="height: 40px;">
                                            <div class="progress-bar  bg-success" style="width: 100%" role="progressbar">
                                            <h5 style="padding-top:5px;"><strong>100 %</strong></h5>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                        <h5 class="card-title text-uppercase text-white text-center bg-info">Request Headers</h5>
                                        <div class="table-responsive">
                                            <table class="table table-bordered">
                                            <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Type</td>
                                                        <td>application/json</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">User-Agent</td>
                                                        <td>PostmanRuntime/7.29.0</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept</td>
                                                        <td>*/*</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cache-Control</td>
                                                        <td>no-cache</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Postman-Token</td>
                                                        <td>5c0f86a1-f271-495f-9368-4145f929b693</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Host</td>
                                                        <td>bootcampapi.techcs.io</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept-Encoding</td>
                                                        <td>gzip, deflate, br</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Connection</td>
                                                        <td>keep-alive</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Length</td>
                                                        <td>62</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cookie</td>
                                                        <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRlbmVtZUBkYi5jb20iLCJpZCI6IjVGbVYzOER0QkJUYk9HYkUxZnB3IiwiaWF0IjoxNjQyNTA4MjQ5fQ.dT8YG0UHLNcxwTcyvuMm4lgAzb3WgpAztjaXnpc_nLk</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Body</h5>
                                        <div class="dyn-height">
                                            <pre><code id="copyReqText-5" class="prettyPrint">{
          &quot;email&quot;: &quot;&quot;,
          &quot;password&quot;: &quot;pznkq5afp3ff3d2sd7wp947u&quot;
        }</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyReqText-5">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Headers</h5>
                                    <div class="table-responsive">
                                        <table class="table table-bordered">
                                        <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-nowrap">Content-Type</td>
                                                    <td>application/json; charset&#x3D;utf-8</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Content-Length</td>
                                                    <td>163</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Connection</td>
                                                    <td>keep-alive</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-powered-by</td>
                                                    <td>Express</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">access-control-allow-origin</td>
                                                    <td>*</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">etag</td>
                                                    <td>W/&quot;a3-3N6+RI35CcEVMLrktlnlQDdaqGk&quot;</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">date</td>
                                                    <td>Tue, 18 Jan 2022 12:17:30 GMT</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-envoy-upstream-service-time</td>
                                                    <td>2</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">server</td>
                                                    <td>istio-envoy</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Cache</td>
                                                    <td>Error from cloudfront</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Via</td>
                                                    <td>1.1 a267c4458d5587daaaf85f1d134a02d4.cloudfront.net (CloudFront)</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Pop</td>
                                                    <td>FRA50-C1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Id</td>
                                                    <td>iEzE0nScS83gplMIArNMhjljHFUrTuxanaXOBK6wSi_tIoz-Mx4tJg&#x3D;&#x3D;</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Body</h5>
                                        <div class="dyn-height">
                                                <pre><code id="copyText-166254a8-0a70-4478-b928-8f09a0e0c4b2" class="prettyPrint">{&quot;statusCode&quot;:400,&quot;message&quot;:[&quot;email should not be empty&quot;,&quot;email must be an email&quot;,&quot;password must be shorter than or equal to 20 characters&quot;],&quot;error&quot;:&quot;Bad Request&quot;}</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyText-166254a8-0a70-4478-b928-8f09a0e0c4b2">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="card border-info">
                                <div class="card-body">
                                <h5 class="card-title text-uppercase text-white text-center bg-info">Test Information</h5>
                                    <div class="table-responsive text-nowrap">
                                        <table id="myTable-166254a8-0a70-4478-b928-8f09a0e0c4b2" class="table table-hover">
                                        <thead><tr class="text-center"><th>Name</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead>
                                            <tbody>
                                                <tr >
                                                    <td >Request Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Response Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Request Body Invalid Field Errors Case: emptyEmail, invalidPassword</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Status Code is 400</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-light">
                                                    <td><strong>Total</strong></td>
                                                    <td class="text-center">4</td>
                                                    <td class="text-center">0</td>
                                                    <td class="text-center">0</td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>
                                    <div class="row d-none">
                                    <div class="col-sm-12 mb-3">
                                        <div class="card-deck">
                                        <div class="card border-danger" style="width: 50rem;">
                                            <div class="card-body">
                                                <h5 class="card-title text-uppercase text-white text-center bg-danger">Test Failure</h5>
                                                <div class="table-responsive">
                                                    <table class="table table-hover">
                                                    <thead><tr class="text-nowrap"><th>Test Name</th><th>Assertion Error</th></tr></thead>
                                                        <tbody>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <div id="folder-fc2c4196-d144-4407-8feb-61b20400b2fb" class="card-deck iteration-0">
            <div class="row iteration-0">
                <div class="col-sm-12 mb-3 iteration-0">
                <div class="card iteration-0">
                    <div class="card-header  bg-success iteration-0">
                        <a data-toggle="collapse" href="#" data-target="#collapse-fc2c4196-d144-4407-8feb-61b20400b2fb" aria-expanded="false" aria-controls="collapse" id="requests-fc2c4196-d144-4407-8feb-61b20400b2fb" class="collapsed text-white z-block">
                    Iteration: 1 - Sign Up Fail - Invalid Fields <i class="float-lg-right fa fa-chevron-down" style="padding-top: 5px;"></i>
                </a>
                    </div>
                    <div id="collapse-fc2c4196-d144-4407-8feb-61b20400b2fb" class="collapse" aria-labelledby="requests-fc2c4196-d144-4407-8feb-61b20400b2fb">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request Method:</strong> <span class="badge-outline-success badge badge-success"> POST</span><br>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request URL:</strong> <a href="https://bootcampapi.techcs.io/api/fe/v1/authorization/signup" target="_blank">https://bootcampapi.techcs.io/api/fe/v1/authorization/signup</a><br>
                                    </div>
                                </div>
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Response Code:</strong> <span class="float-right badge-outline badge badge-success"> 400 - Bad Request</span><br>
                                    <span><i class="fas fa-stopwatch"></i></span><strong> Mean time per request:</strong> <span class="float-right badge-outline badge badge-success"> 62ms</span><br>
                                    <span><i class="fas fa-database"></i></span><strong> Mean size per request:</strong> <span class="float-right badge-outline badge badge-success"> 192B</span><br>
                                    <hr>
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Test Pass Percentage</h5>
                                    <div>
                                        <div class="progress" style="height: 40px;">
                                            <div class="progress-bar  bg-success" style="width: 100%" role="progressbar">
                                            <h5 style="padding-top:5px;"><strong>100 %</strong></h5>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                        <h5 class="card-title text-uppercase text-white text-center bg-info">Request Headers</h5>
                                        <div class="table-responsive">
                                            <table class="table table-bordered">
                                            <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Type</td>
                                                        <td>application/json</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">User-Agent</td>
                                                        <td>PostmanRuntime/7.29.0</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept</td>
                                                        <td>*/*</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cache-Control</td>
                                                        <td>no-cache</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Postman-Token</td>
                                                        <td>45b3d2b9-a764-4b80-8889-106610400e24</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Host</td>
                                                        <td>bootcampapi.techcs.io</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept-Encoding</td>
                                                        <td>gzip, deflate, br</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Connection</td>
                                                        <td>keep-alive</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Length</td>
                                                        <td>38</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cookie</td>
                                                        <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRlbmVtZUBkYi5jb20iLCJpZCI6IjVGbVYzOER0QkJUYk9HYkUxZnB3IiwiaWF0IjoxNjQyNTA4MjQ5fQ.dT8YG0UHLNcxwTcyvuMm4lgAzb3WgpAztjaXnpc_nLk</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Body</h5>
                                        <div class="dyn-height">
                                            <pre><code id="copyReqText-6" class="prettyPrint">{
          &quot;email&quot;: &quot;&quot;,
          &quot;password&quot;: &quot;&quot;
        }</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyReqText-6">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Headers</h5>
                                    <div class="table-responsive">
                                        <table class="table table-bordered">
                                        <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-nowrap">Content-Type</td>
                                                    <td>application/json; charset&#x3D;utf-8</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Content-Length</td>
                                                    <td>192</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Connection</td>
                                                    <td>keep-alive</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-powered-by</td>
                                                    <td>Express</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">access-control-allow-origin</td>
                                                    <td>*</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">etag</td>
                                                    <td>W/&quot;c0-Y3CJBMuY9+uKqpzHLsMgNy/U4xU&quot;</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">date</td>
                                                    <td>Tue, 18 Jan 2022 12:17:30 GMT</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-envoy-upstream-service-time</td>
                                                    <td>1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">server</td>
                                                    <td>istio-envoy</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Cache</td>
                                                    <td>Error from cloudfront</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Via</td>
                                                    <td>1.1 a267c4458d5587daaaf85f1d134a02d4.cloudfront.net (CloudFront)</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Pop</td>
                                                    <td>FRA50-C1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Id</td>
                                                    <td>Ni2S4D__7Rq0r19DQAsT6GBdn3LIhKeUS_QlkUnzYoUVpiVWeI3KZw&#x3D;&#x3D;</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Body</h5>
                                        <div class="dyn-height">
                                                <pre><code id="copyText-166254a8-0a70-4478-b928-8f09a0e0c4b2" class="prettyPrint">{&quot;statusCode&quot;:400,&quot;message&quot;:[&quot;email should not be empty&quot;,&quot;email must be an email&quot;,&quot;password must be longer than or equal to 8 characters&quot;,&quot;password should not be empty&quot;],&quot;error&quot;:&quot;Bad Request&quot;}</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyText-166254a8-0a70-4478-b928-8f09a0e0c4b2">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="card border-info">
                                <div class="card-body">
                                <h5 class="card-title text-uppercase text-white text-center bg-info">Test Information</h5>
                                    <div class="table-responsive text-nowrap">
                                        <table id="myTable-166254a8-0a70-4478-b928-8f09a0e0c4b2" class="table table-hover">
                                        <thead><tr class="text-center"><th>Name</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead>
                                            <tbody>
                                                <tr >
                                                    <td >Request Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Response Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Request Body Invalid Field Errors Case: emptyEmail, emptyPassword</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Status Code is 400</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-light">
                                                    <td><strong>Total</strong></td>
                                                    <td class="text-center">4</td>
                                                    <td class="text-center">0</td>
                                                    <td class="text-center">0</td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>
                                    <div class="row d-none">
                                    <div class="col-sm-12 mb-3">
                                        <div class="card-deck">
                                        <div class="card border-danger" style="width: 50rem;">
                                            <div class="card-body">
                                                <h5 class="card-title text-uppercase text-white text-center bg-danger">Test Failure</h5>
                                                <div class="table-responsive">
                                                    <table class="table table-hover">
                                                    <thead><tr class="text-nowrap"><th>Test Name</th><th>Assertion Error</th></tr></thead>
                                                        <tbody>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <div id="folder-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7" class="card-deck iteration-0">
            <div class="row iteration-0">
                <div class="col-sm-12 mb-3 iteration-0">
                <div class="card iteration-0">
                    <div class="card-header  bg-success iteration-0">
                        <a data-toggle="collapse" href="#" data-target="#collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7" aria-expanded="false" aria-controls="collapse" id="requests-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7" class="collapsed text-white z-block">
                    Iteration: 1 - Sign Up Fail - User Already Signed-Up <i class="float-lg-right fa fa-chevron-down" style="padding-top: 5px;"></i>
                </a>
                    </div>
                    <div id="collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7" class="collapse" aria-labelledby="requests-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request Method:</strong> <span class="badge-outline-success badge badge-success"> POST</span><br>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Request URL:</strong> <a href="https://bootcampapi.techcs.io/api/fe/v1/authorization/signup" target="_blank">https://bootcampapi.techcs.io/api/fe/v1/authorization/signup</a><br>
                                    </div>
                                </div>
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Information</h5>
                                    <span><i class="fas fa-info-circle"></i></span><strong> Response Code:</strong> <span class="float-right badge-outline badge badge-success"> 409 - Conflict</span><br>
                                    <span><i class="fas fa-stopwatch"></i></span><strong> Mean time per request:</strong> <span class="float-right badge-outline badge badge-success"> 145ms</span><br>
                                    <span><i class="fas fa-database"></i></span><strong> Mean size per request:</strong> <span class="float-right badge-outline badge badge-success"> 69B</span><br>
                                    <hr>
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Test Pass Percentage</h5>
                                    <div>
                                        <div class="progress" style="height: 40px;">
                                            <div class="progress-bar  bg-success" style="width: 100%" role="progressbar">
                                            <h5 style="padding-top:5px;"><strong>100 %</strong></h5>
                                            </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 mb-3">
                                <div class="card-deck">
                                <div class="card border-info" style="width: 50rem;">
                                    <div class="card-body">
                                        <h5 class="card-title text-uppercase text-white text-center bg-info">Request Headers</h5>
                                        <div class="table-responsive">
                                            <table class="table table-bordered">
                                            <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Type</td>
                                                        <td>application/json</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">User-Agent</td>
                                                        <td>PostmanRuntime/7.29.0</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept</td>
                                                        <td>*/*</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cache-Control</td>
                                                        <td>no-cache</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Postman-Token</td>
                                                        <td>1b6f09ed-66ff-4eb1-bc7d-69df5d42bc8a</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Host</td>
                                                        <td>bootcampapi.techcs.io</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Accept-Encoding</td>
                                                        <td>gzip, deflate, br</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Connection</td>
                                                        <td>keep-alive</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Content-Length</td>
                                                        <td>59</td>
                                                    </tr>
                                                    <tr>
                                                        <td class="text-nowrap">Cookie</td>
                                                        <td>auth_token&#x3D;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRlbmVtZUBkYi5jb20iLCJpZCI6IjVGbVYzOER0QkJUYk9HYkUxZnB3IiwiaWF0IjoxNjQyNTA4MjQ5fQ.dT8YG0UHLNcxwTcyvuMm4lgAzb3WgpAztjaXnpc_nLk</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Request Body</h5>
                                        <div class="dyn-height">
                                            <pre><code id="copyReqText-7" class="prettyPrint">{
          &quot;email&quot;: &quot;deneme@db.com&quot;,
          &quot;password&quot;: &quot;12345678&quot;
        }</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyReqText-7">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Headers</h5>
                                    <div class="table-responsive">
                                        <table class="table table-bordered">
                                        <thead class="thead-light text-center"><tr><th>Header Name</th><th>Header Value</th></tr></thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-nowrap">Content-Type</td>
                                                    <td>application/json; charset&#x3D;utf-8</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Content-Length</td>
                                                    <td>69</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Connection</td>
                                                    <td>keep-alive</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-powered-by</td>
                                                    <td>Express</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">access-control-allow-origin</td>
                                                    <td>*</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">etag</td>
                                                    <td>W/&quot;45-Qy9MnxcVj5tUQbarcdsE+EEMjo0&quot;</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">date</td>
                                                    <td>Tue, 18 Jan 2022 12:17:30 GMT</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">x-envoy-upstream-service-time</td>
                                                    <td>88</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">server</td>
                                                    <td>istio-envoy</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Cache</td>
                                                    <td>Error from cloudfront</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">Via</td>
                                                    <td>1.1 a267c4458d5587daaaf85f1d134a02d4.cloudfront.net (CloudFront)</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Pop</td>
                                                    <td>FRA50-C1</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-nowrap">X-Amz-Cf-Id</td>
                                                    <td>vzsKQ2DD6XIira5bVocauhGLf-E4CRUC4K7FSoFyWrIV2S0NQMAMcg&#x3D;&#x3D;</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div class="row">
                        <div class="col-sm-12 mb-3">
                            <div class="card-deck">
                            <div class="card border-info" style="width: 50rem;">
                                <div class="card-body">
                                    <h5 class="card-title text-uppercase text-white text-center bg-info">Response Body</h5>
                                        <div class="dyn-height">
                                                <pre><code id="copyText-3b9b1065-33fb-46d2-b383-93aaa9421c19" class="prettyPrint">{&quot;statusCode&quot;:409,&quot;message&quot;:&quot;User already exist!&quot;,&quot;error&quot;:&quot;Conflict&quot;}</code></pre>
                                        </div>
                                        <div class="card-footer">
                                            <button class="btn btn-outline-secondary btn-sm copyButton" type="button" data-clipboard-action="copy" data-clipboard-target="#copyText-3b9b1065-33fb-46d2-b383-93aaa9421c19">Copy to Clipboard</button>
                                        </div>
                                </div>
                            </div>
                            </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="card border-info">
                                <div class="card-body">
                                <h5 class="card-title text-uppercase text-white text-center bg-info">Test Information</h5>
                                    <div class="table-responsive text-nowrap">
                                        <table id="myTable-3b9b1065-33fb-46d2-b383-93aaa9421c19" class="table table-hover">
                                        <thead><tr class="text-center"><th>Name</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead>
                                            <tbody>
                                                <tr >
                                                    <td >Request Body Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Response Body Types are Valid</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Unsuccessful Sign Up</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                                <tr >
                                                    <td >Status Code is 409</td>
                                                    <td class="text-center bg-success">1</td>
                                                    <td class="text-center ">0</td>
                                                    <td class="text-center ">0</td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-light">
                                                    <td><strong>Total</strong></td>
                                                    <td class="text-center">4</td>
                                                    <td class="text-center">0</td>
                                                    <td class="text-center">0</td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>
                                    <div class="row d-none">
                                    <div class="col-sm-12 mb-3">
                                        <div class="card-deck">
                                        <div class="card border-danger" style="width: 50rem;">
                                            <div class="card-body">
                                                <h5 class="card-title text-uppercase text-white text-center bg-danger">Test Failure</h5>
                                                <div class="table-responsive">
                                                    <table class="table table-hover">
                                                    <thead><tr class="text-nowrap"><th>Test Name</th><th>Assertion Error</th></tr></thead>
                                                        <tbody>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
    </div>
    </div>
    </div>
    </div>
    </div>
</body>
</html>


<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.2.1/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.datatables.net/v/bs4/dt-1.10.18/datatables.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/remarkable/1.7.1/remarkable.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>

<!-- Data Table Configuration -->

<script>
$(document).ready( function () {
    $('#myTable-ce3aa8db-1800-462d-88b2-3bd4d965a634').DataTable({
        "retrieve": true,
        "paging": false,
        "info": false,
        "fixedColumns":   {
            "heightMatch": 'none'
        }
    });
});
$(document).ready( function () {
    $('#myTable-72e041c4-4d3a-4d88-8fd1-aef735edaf14').DataTable({
        "retrieve": true,
        "paging": false,
        "info": false,
        "fixedColumns":   {
            "heightMatch": 'none'
        }
    });
});
$(document).ready( function () {
    $('#myTable-1fd7a490-feb8-4ca0-a784-86fec75f8367').DataTable({
        "retrieve": true,
        "paging": false,
        "info": false,
        "fixedColumns":   {
            "heightMatch": 'none'
        }
    });
});
$(document).ready( function () {
    $('#myTable-166254a8-0a70-4478-b928-8f09a0e0c4b2').DataTable({
        "retrieve": true,
        "paging": false,
        "info": false,
        "fixedColumns":   {
            "heightMatch": 'none'
        }
    });
});
$(document).ready( function () {
    $('#myTable-166254a8-0a70-4478-b928-8f09a0e0c4b2').DataTable({
        "retrieve": true,
        "paging": false,
        "info": false,
        "fixedColumns":   {
            "heightMatch": 'none'
        }
    });
});
$(document).ready( function () {
    $('#myTable-166254a8-0a70-4478-b928-8f09a0e0c4b2').DataTable({
        "retrieve": true,
        "paging": false,
        "info": false,
        "fixedColumns":   {
            "heightMatch": 'none'
        }
    });
});
$(document).ready( function () {
    $('#myTable-166254a8-0a70-4478-b928-8f09a0e0c4b2').DataTable({
        "retrieve": true,
        "paging": false,
        "info": false,
        "fixedColumns":   {
            "heightMatch": 'none'
        }
    });
});
$(document).ready( function () {
    $('#myTable-3b9b1065-33fb-46d2-b383-93aaa9421c19').DataTable({
        "retrieve": true,
        "paging": false,
        "info": false,
        "fixedColumns":   {
            "heightMatch": 'none'
        }
    });
});
</script>

<!-- Tooltip Configuration -->

<script>
$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip({
        trigger : 'hover'
    })
})
</script>

<!-- Show/Hide The Folders -->

<script>
$('#openAll').on('click', function(e) {
let clickCount = $(this).data("clickCount") || 1
switch (clickCount){
    case 1:
            $('#folder-5ca7a9bb-a49f-45e8-baca-fec51b52a237-iteration-0').removeClass('collapsed')
            $('#folder-collapse-5ca7a9bb-a49f-45e8-baca-fec51b52a237-iteration-0').addClass('show')
        $('#openAll').html("Collapse Folders");
        break;
    case 2:
            $('#folder-5ca7a9bb-a49f-45e8-baca-fec51b52a237-iteration-0').addClass('collapsed')
            $('#folder-collapse-5ca7a9bb-a49f-45e8-baca-fec51b52a237-iteration-0').removeClass('show')
        $('#openAll').html("Expand Folders");
        break;
}
clickCount = clickCount > 1 ? 1 : ++clickCount;
$(this).data("clickCount", clickCount)
})
</script>

<!-- Show/Hide The Requests -->

<script>
$('#openAllRequests').on('click', function(e) {
let clickCount = $(this).data("clickCount") || 1
switch (clickCount){
    case 1:
            $('#requests-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').removeClass('collapsed')
            $('#collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').removeClass('collapsed')
            $('#requests-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').addClass('show')
            $('#collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').addClass('show')
            $('#requests-ec44a978-2098-4b07-9d9f-9673b796b143').removeClass('collapsed')
            $('#collapse-ec44a978-2098-4b07-9d9f-9673b796b143').removeClass('collapsed')
            $('#requests-ec44a978-2098-4b07-9d9f-9673b796b143').addClass('show')
            $('#collapse-ec44a978-2098-4b07-9d9f-9673b796b143').addClass('show')
            $('#requests-d3a8c81d-df29-454a-b204-19cc424d5d1c').removeClass('collapsed')
            $('#collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c').removeClass('collapsed')
            $('#requests-d3a8c81d-df29-454a-b204-19cc424d5d1c').addClass('show')
            $('#collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c').addClass('show')
            $('#requests-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').removeClass('collapsed')
            $('#collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').removeClass('collapsed')
            $('#requests-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').addClass('show')
            $('#collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').addClass('show')
            $('#requests-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').removeClass('collapsed')
            $('#collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').removeClass('collapsed')
            $('#requests-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').addClass('show')
            $('#collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').addClass('show')
            $('#requests-0349d8d7-9111-4d8b-836e-998cfc8312a3').removeClass('collapsed')
            $('#collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3').removeClass('collapsed')
            $('#requests-0349d8d7-9111-4d8b-836e-998cfc8312a3').addClass('show')
            $('#collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3').addClass('show')
            $('#requests-fc2c4196-d144-4407-8feb-61b20400b2fb').removeClass('collapsed')
            $('#collapse-fc2c4196-d144-4407-8feb-61b20400b2fb').removeClass('collapsed')
            $('#requests-fc2c4196-d144-4407-8feb-61b20400b2fb').addClass('show')
            $('#collapse-fc2c4196-d144-4407-8feb-61b20400b2fb').addClass('show')
            $('#requests-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').removeClass('collapsed')
            $('#collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').removeClass('collapsed')
            $('#requests-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').addClass('show')
            $('#collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').addClass('show')
        $('#openAllRequests').html("Collapse Requests");
        break;
    case 2:
            $('#requests-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').addClass('collapsed')
            $('#collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').addClass('collapsed')
            $('#requests-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').removeClass('show')
            $('#collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').removeClass('show')
            $('#requests-ec44a978-2098-4b07-9d9f-9673b796b143').addClass('collapsed')
            $('#collapse-ec44a978-2098-4b07-9d9f-9673b796b143').addClass('collapsed')
            $('#requests-ec44a978-2098-4b07-9d9f-9673b796b143').removeClass('show')
            $('#collapse-ec44a978-2098-4b07-9d9f-9673b796b143').removeClass('show')
            $('#requests-d3a8c81d-df29-454a-b204-19cc424d5d1c').addClass('collapsed')
            $('#collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c').addClass('collapsed')
            $('#requests-d3a8c81d-df29-454a-b204-19cc424d5d1c').removeClass('show')
            $('#collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c').removeClass('show')
            $('#requests-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').addClass('collapsed')
            $('#collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').addClass('collapsed')
            $('#requests-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').removeClass('show')
            $('#collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').removeClass('show')
            $('#requests-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').addClass('collapsed')
            $('#collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').addClass('collapsed')
            $('#requests-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').removeClass('show')
            $('#collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').removeClass('show')
            $('#requests-0349d8d7-9111-4d8b-836e-998cfc8312a3').addClass('collapsed')
            $('#collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3').addClass('collapsed')
            $('#requests-0349d8d7-9111-4d8b-836e-998cfc8312a3').removeClass('show')
            $('#collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3').removeClass('show')
            $('#requests-fc2c4196-d144-4407-8feb-61b20400b2fb').addClass('collapsed')
            $('#collapse-fc2c4196-d144-4407-8feb-61b20400b2fb').addClass('collapsed')
            $('#requests-fc2c4196-d144-4407-8feb-61b20400b2fb').removeClass('show')
            $('#collapse-fc2c4196-d144-4407-8feb-61b20400b2fb').removeClass('show')
            $('#requests-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').addClass('collapsed')
            $('#collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').addClass('collapsed')
            $('#requests-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').removeClass('show')
            $('#collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').removeClass('show')
        $('#openAllRequests').html("Expand Requests");
        break;
}
clickCount = clickCount > 1 ? 1 : ++clickCount;
$(this).data("clickCount", clickCount)
})
</script>

<!-- Show/Hide The Skipped Tests -->

<script>
$('#openAllSkipped').on('click', function(e) {
let clickCount = $(this).data("clickCount") || 1
switch (clickCount){
    case 1:
            $('#skipped-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').removeClass('collapsed')
            $('#skipped-collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').removeClass('collapsed')
            $('#skipped-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').addClass('show')
            $('#skipped-collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').addClass('show')
            $('#skipped-ec44a978-2098-4b07-9d9f-9673b796b143').removeClass('collapsed')
            $('#skipped-collapse-ec44a978-2098-4b07-9d9f-9673b796b143').removeClass('collapsed')
            $('#skipped-ec44a978-2098-4b07-9d9f-9673b796b143').addClass('show')
            $('#skipped-collapse-ec44a978-2098-4b07-9d9f-9673b796b143').addClass('show')
            $('#skipped-d3a8c81d-df29-454a-b204-19cc424d5d1c').removeClass('collapsed')
            $('#skipped-collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c').removeClass('collapsed')
            $('#skipped-d3a8c81d-df29-454a-b204-19cc424d5d1c').addClass('show')
            $('#skipped-collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c').addClass('show')
            $('#skipped-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').removeClass('collapsed')
            $('#skipped-collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').removeClass('collapsed')
            $('#skipped-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').addClass('show')
            $('#skipped-collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').addClass('show')
            $('#skipped-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').removeClass('collapsed')
            $('#skipped-collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').removeClass('collapsed')
            $('#skipped-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').addClass('show')
            $('#skipped-collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').addClass('show')
            $('#skipped-0349d8d7-9111-4d8b-836e-998cfc8312a3').removeClass('collapsed')
            $('#skipped-collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3').removeClass('collapsed')
            $('#skipped-0349d8d7-9111-4d8b-836e-998cfc8312a3').addClass('show')
            $('#skipped-collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3').addClass('show')
            $('#skipped-fc2c4196-d144-4407-8feb-61b20400b2fb').removeClass('collapsed')
            $('#skipped-collapse-fc2c4196-d144-4407-8feb-61b20400b2fb').removeClass('collapsed')
            $('#skipped-fc2c4196-d144-4407-8feb-61b20400b2fb').addClass('show')
            $('#skipped-collapse-fc2c4196-d144-4407-8feb-61b20400b2fb').addClass('show')
            $('#skipped-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').removeClass('collapsed')
            $('#skipped-collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').removeClass('collapsed')
            $('#skipped-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').addClass('show')
            $('#skipped-collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').addClass('show')
        $('#openAllSkipped').html("Collapse All Skipped Tests");
        break;
    case 2:
            $('#skipped-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').addClass('collapsed')
            $('#skipped-collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').addClass('collapsed')
            $('#skipped-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').removeClass('show')
            $('#skipped-collapse-e0b8a0c9-e22d-4ad4-8bb4-cf6d9807c68a').removeClass('show')
            $('#skipped-ec44a978-2098-4b07-9d9f-9673b796b143').addClass('collapsed')
            $('#skipped-collapse-ec44a978-2098-4b07-9d9f-9673b796b143').addClass('collapsed')
            $('#skipped-ec44a978-2098-4b07-9d9f-9673b796b143').removeClass('show')
            $('#skipped-collapse-ec44a978-2098-4b07-9d9f-9673b796b143').removeClass('show')
            $('#skipped-d3a8c81d-df29-454a-b204-19cc424d5d1c').addClass('collapsed')
            $('#skipped-collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c').addClass('collapsed')
            $('#skipped-d3a8c81d-df29-454a-b204-19cc424d5d1c').removeClass('show')
            $('#skipped-collapse-d3a8c81d-df29-454a-b204-19cc424d5d1c').removeClass('show')
            $('#skipped-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').addClass('collapsed')
            $('#skipped-collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').addClass('collapsed')
            $('#skipped-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').removeClass('show')
            $('#skipped-collapse-77e93a24-8b1e-414b-8f45-ab96fd6f6f5c').removeClass('show')
            $('#skipped-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').addClass('collapsed')
            $('#skipped-collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').addClass('collapsed')
            $('#skipped-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').removeClass('show')
            $('#skipped-collapse-6e63495a-be99-4ffb-9510-4dfe84bfe1f6').removeClass('show')
            $('#skipped-0349d8d7-9111-4d8b-836e-998cfc8312a3').addClass('collapsed')
            $('#skipped-collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3').addClass('collapsed')
            $('#skipped-0349d8d7-9111-4d8b-836e-998cfc8312a3').removeClass('show')
            $('#skipped-collapse-0349d8d7-9111-4d8b-836e-998cfc8312a3').removeClass('show')
            $('#skipped-fc2c4196-d144-4407-8feb-61b20400b2fb').addClass('collapsed')
            $('#skipped-collapse-fc2c4196-d144-4407-8feb-61b20400b2fb').addClass('collapsed')
            $('#skipped-fc2c4196-d144-4407-8feb-61b20400b2fb').removeClass('show')
            $('#skipped-collapse-fc2c4196-d144-4407-8feb-61b20400b2fb').removeClass('show')
            $('#skipped-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').addClass('collapsed')
            $('#skipped-collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').addClass('collapsed')
            $('#skipped-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').removeClass('show')
            $('#skipped-collapse-ea4825a0-5ba3-4e56-9472-a10ffb4a72a7').removeClass('show')
        $('#openAllSkipped').html("Expand All Skipped Tests");
        break;
}
clickCount = clickCount > 1 ? 1 : ++clickCount;
$(this).data("clickCount", clickCount)
})
</script>

<!-- Show/Hide The Failures -->

<script>
$('#openAllFailed').on('click', function(e) {
let clickCount = $(this).data("clickCount") || 1
let failedItemContent
let failedItemHeading
switch (clickCount){
    case 1:
            failedItemHeading = $('#fails-c657f7d8-6085-43f2-b982-fad4f04c4eee');
            failedItemContent = $("#fails-collapse-c657f7d8-6085-43f2-b982-fad4f04c4eee");
            failedItemHeading.removeClass('collapsed')
            failedItemContent.removeClass('collapsed')
            failedItemHeading.addClass('show')
            failedItemContent.addClass('show')
            failedItemHeading = $('#fails-6cdb60b5-a078-44af-a198-e8ec4344ba1c');
            failedItemContent = $("#fails-collapse-6cdb60b5-a078-44af-a198-e8ec4344ba1c");
            failedItemHeading.removeClass('collapsed')
            failedItemContent.removeClass('collapsed')
            failedItemHeading.addClass('show')
            failedItemContent.addClass('show')
        $('#openAllFailed').html("Collapse All Failed Tests");
        break;
    case 2:
            failedItemHeading = $('#fails-c657f7d8-6085-43f2-b982-fad4f04c4eee');
            failedItemContent = $("#fails-collapse-c657f7d8-6085-43f2-b982-fad4f04c4eee");
            failedItemHeading.removeClass('show')
            failedItemContent.removeClass('show')
            failedItemHeading.addClass('collapsed')
            failedItemContent.addClass('collapsed')
            failedItemHeading = $('#fails-6cdb60b5-a078-44af-a198-e8ec4344ba1c');
            failedItemContent = $("#fails-collapse-6cdb60b5-a078-44af-a198-e8ec4344ba1c");
            failedItemHeading.removeClass('show')
            failedItemContent.removeClass('show')
            failedItemHeading.addClass('collapsed')
            failedItemContent.addClass('collapsed')
        $('#openAllFailed').html("Expand All Failed Tests");
        break;
}
clickCount = clickCount > 1 ? 1 : ++clickCount;
$(this).data("clickCount", clickCount)
})
</script>

<!-- Pretty Print the Response Body-->

<script>
function isJSON(data)
{
    var ret = true;
    try {
            JSON.parse(data);
    }catch(e) {
            ret = false;
    }
    return ret;
}

function isXML(data)
{
    return (data.length > 0 && data[0] === '<');
}

// see https://gist.github.com/sente/1083506/d2834134cd070dbcc08bf42ee27dabb746a1c54d#gistcomment-2254622
function formatXML(data) {
    const PADDING = ' '.repeat(2); // set desired indent size here
    const reg = /(>)(<)(\/*)/g;
    let pad = 0;
    xml = data.replace(reg, '$1\r\n$2$3');

    return xml.split('\r\n').map((node, index) => {
        let indent = 0;
        if (node.match(/.+<\/\w[^>]*>$/)) {
            indent = 0;
        } else if (node.match(/^<\/\w/) && pad > 0) {
            pad -= 1;
        } else if (node.match(/^<\w[^>]*[^\/]>.*$/)) {
            indent = 1;
        } else {
            indent = 0;
        }

        pad += indent;
        return PADDING.repeat(pad - indent) + node;
    }).join('\r\n');
}

$(".prettyPrint").each(function () {
        var data = $(this).text();
        // Verify whether data is JSON
        if(isJSON(data))
        {
                obj = JSON.parse(data);
                data = JSON.stringify(obj, null, 2);
        }
        else if(isXML(data)) {
            data = formatXML(data);            
        }
        $(this).text(data);
});
</script>


<!-- Copy Response Body To Clipboard -->

<script>
    var clipboard = new ClipboardJS('.copyButton');

    clipboard.on('success', function(e) {
        e.clearSelection();
        $(".copyButton").addClass("bg-success text-white")
        e.trigger.textContent = '✔ Copied!';
        window.setTimeout(function() {
            $(".copyButton").removeClass("bg-success text-white")
            e.trigger.textContent = 'Copy to Clipboard';
        }, 2000);
    });
    clipboard.on('error', function(e) {
        e.clearSelection();
        $(".copyButton").addClass("bg-danger text-white")
        e.trigger.textContent = '✗ Not Copied';
        window.setTimeout(function() {
            $(".copyButton").removeClass("bg-danger text-white")
            e.trigger.textContent = 'Copy to Clipboard';
        }, 2000);
    });

</script>

<!-- Render the Description Markdown and link in the test failures -->

<script>
    const remarkable = new Remarkable();

    const descriptions = document.querySelectorAll(".renderMarkdown");
    descriptions.forEach(description => {
        description.innerHTML = renderHtmlFromMarkdown(description.textContent);
    });
    function renderHtmlFromMarkdown(markdown) {
        return remarkable.render(trim(markdown));
    }
    function trim(string) {
        return string ? string.replace(/^ +| +$/gm, "") : string;
    }
</script>

<!-- Show/Hide The Toggles When Scrolling The Page -->

<script>
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("topOfRequestsScreen").style.display = "block";
    document.getElementById("topOfFailuresScreen").style.display = "block";
    document.getElementById("topOfSkippedScreen").style.display = "block";
    document.getElementById("openAll").style.display = "none";
    document.getElementById("openAllRequests").style.display = "none";
    
    
    document.getElementById("showOnlyFailures").style.display = "none";
    document.getElementById("openAllFailed").style.display = "none";
  } else {
    document.getElementById("topOfRequestsScreen").style.display = "none";
    document.getElementById("topOfFailuresScreen").style.display = "none";
    document.getElementById("topOfSkippedScreen").style.display = "none";
    document.getElementById("openAll").style.display = "block";
    document.getElementById("openAllRequests").style.display = "block";
    
    document.getElementById("showOnlyFailures").style.display = "block";
    document.getElementById("openAllFailed").style.display = "block";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
</script>

<!-- Creates The Iteration Tabs -->

<script type="text/javascript">
    "use strict";

window.onload = function () {

  // set display for all blocks of response
  var allItems = document.querySelectorAll('[class*=iteration-]');
  allItems.forEach(function(elem){
    elem.style.display = 'block';
  });

   
  let totalIterations = 1;
   

  let menu = document.querySelector('#execution-menu .nav');

  for(var i = 0; i < totalIterations; i++)
  {
    let li = document.createElement('li');
    li.appendChild(document.createTextNode((i + 1)));
    li.setAttribute('id', 'iteration-' + i);
    li.classList.add("custom-tab");
    li.classList.add("itPassed");

    li.addEventListener('click', function() {
      //set display to none for all except row
      let allItems = document.querySelectorAll('[class*=iteration-]:not(.row)');
      allItems.forEach(function(elem) {
        elem.style.display = 'none';
      })

      let allMenus = document.querySelectorAll('[id*=iteration-]');
      allMenus.forEach(function(elem){
        elem.style.borderBottom = 'none';
      })
    
      this.style.borderBottom = 'solid 3px #032a33';

      let items = document.querySelectorAll("." + this.id + ':not(.row)');
      items.forEach(function(elem) {
        elem.style.display = elem.style.display == 'block' ? 'none' : 'block';
      })
    });
    menu.appendChild(li);
  }

  //shows first tab data
  document.getElementById('iteration-0').click();
  document.getElementById('iterationSelected').innerHTML = `Iteration ${document.getElementById('iteration-0').innerHTML} selected`

    $("#iteration-0").removeClass('itPassed').addClass('itFailed')
    $("#iteration-0").removeClass('itPassed').addClass('itFailed')
}
</script>

<!-- Create the Selected Iteration Label -->

<script>
$(document).ready(function(){
    $(function() {
        $("#iterationList li").click(function() {
            document.getElementById('iterationSelected').innerHTML = "Iteration " + this.innerHTML + " selected"
        });
    });
});
</script>

<!-- Filter Action for the Iterations -->

<script>
$("#filterInput").on("input paste", function() {
    var value = $(this).val();
    $("#iterationList li").filter(function() {
	    $("#showOnlyFailures").data("clickCount") ? $("#showOnlyFailures").click():null;
        $(this).toggle($(this).text().indexOf(value) > -1)
    });
});
</script>

<!-- Showing the Failed Interations -->

<script>
$('#showOnlyFailures').on('click', function(e) {
    let clickCount = $(this).data("clickCount") || 1
	$("#filterInput").val()!="" && clickCount==1 ? $("#filterInput").val('').trigger('input'): null;
    let selectedIteration = $('#iterationList li').filter(function () { 
        return $(this).css('border-bottom').indexOf("solid") > -1 && $(this).hasClass('itFailed');
    });
    selectedIteration.length || clickCount > 1 ? null : $("#iterationList li.itFailed")[0].click()
    $("#iterationList li.itPassed").toggle()
    $("div.bg-success [id*=requests]").parents('[class^="row iteration-"]').toggle();
    clickCount = clickCount > 1 ? 1 : ++clickCount;
    clickCount > 1 ? $("#showOnlyFailures").html("Show All Iterations") : $("#showOnlyFailures").html("Show Failed Iterations");
    $(this).data("clickCount", clickCount)     
})
</script>

<!-- Set The Theme Of The Report -->

<script>
        function setTheme(themeName) {
            localStorage.setItem('theme', themeName);
            document.body.className = themeName;
        }

        function toggleTheme() {
            if (localStorage.getItem('theme') === 'theme-light') {
                setTheme('theme-dark');
            } else {
                setTheme('theme-light');
            }
        }

        (function () {
            if (localStorage.getItem('theme') === 'theme-light') {
                setTheme('theme-light');
                document.getElementById('slider').checked = false;
            } else {
                setTheme('theme-dark');
                document.getElementById('slider').checked = true;
            }
        })();
</script>
```
