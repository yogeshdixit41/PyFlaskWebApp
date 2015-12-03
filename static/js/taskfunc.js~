/*
* Helper method to create XMLHttp Request - Not used
*/

function createRequest() {
  var result = null;
  if (window.XMLHttpRequest) {
    // FireFox, Safari, etc.
    result = new XMLHttpRequest();
    if (typeof result.overrideMimeType != 'undefined') {
      result.overrideMimeType('text/xml'); // Or anything else
    }
  }
  else if (window.ActiveXObject) {
    // MSIE
    result = new ActiveXObject("Microsoft.XMLHTTP");
  } 
  else {
    // No known mechanism -- consider aborting the application
  }
  return result;
}


/*
New Project Method
*/

function createProject(){
  if (!newProject()){
    $('#newProject').modal('hide');
  }
  return false;
}

function importProject(){
  if (!writeProject()){
    $('#importProject').modal('hide');
  }
  return false;
}

function createTask(){
  if (!addTask()){
    $('#addTask').modal('hide');
  }
  return false;
}

function editTask(){
  if (!changeTask()){
    $('#editTask').modal('hide');
  }
  return false;
}


function createResource(){
  if (!addResource()){
    $('#addResources').modal('hide');
  }
  return false;
}

function editResource(){
  if(!changeResource()){
    $('#addResource').modal('hide');
  }
  return false;
}


function newProject() {
    $.getJSON('/project/newProject', {
      pname: $('input[name="pName"]').val(),
      date: $('input[name="date"]').val()
      }, function(data) {
        location.reload();  
      });
    return false;
}

function writeProject(){
  //Call webservice to upload project
  return false;
}

function addTask() {
    $.getJSON('/task/addTask', {
      taskName: $('input[name="taskName"]').val(),
      duration: $('input[name="duration"]').val(),
      optTaskType: $('input[name="optTaskType"]:checked').val(),
      selChild: $('select[id="selChild"]').val(),
      selPred: $('select[id="selPred"]').val(),
      selSucc: $('select[id="selSucc"]').val(),
      selRes: $('select[id="selRes"]').val(),
      taskDescription: $('textarea[name="taskDescription"]').val()
      }, function(data) {
        location.reload();  
        console.log(data.children)
       
        //alert(data);
        });
    return false;
}

function changeTask() {
    $.getJSON('/task/editTask', {
      taskId: $('input[id="idHidden"]').val(),
      taskName: $('input[name="taskName"]').val(),
      duration: $('input[name="duration"]').val(),
      optTaskType: $('input[name="optTaskType"]:checked').val(),
      selChild: $('select[id="selChild"]').val(),
      selPred: $('select[id="selPred"]').val(),
      selSucc: $('select[id="selSucc"]').val(),
      selRes: $('select[id="selRes"]').val(),
      taskDescription: $('textarea[name="taskDescription"]').val()
      }, function(data) {
        location.reload();  
        console.log(data.children)
       
        //alert(data);
        });
    return false;
}

function addResource() {
    $.getJSON('/resource/addResource', {
      resourceName: $('input[name="resourceName"]').val(),
      dailycost: $('input[name="dailycost"]').val(),
      resourceType: $('select[id="resourceType"]').val(),
      allocTask: $('select[id="allocTask"]').val()
      }, function(data) {
        location.reload();          

        console.log(data);
        //alert(data);
        });
    return false;
}

function changeResource(){
  $.getJSON('/resource/editResource', {
      resourceId: $('input[id="idHidden"]').val(),
      resourceName: $('input[name="resourceName"]').val(),
      dailycost: $('input[name="dailycost"]').val(),
      resourceType: $('select[id="resourceType"]').val(),
      allocTask: $('select[id="allocTask"]').val()
      }, function(data) {
        location.reload();          

        console.log(data);
        //alert(data);
        });
    return false;
}


function addDeliverable() {
    $.getJSON('/deliverable/addDeliverable', {
      deliverableName: $('input[name="deliverableName"]').val(),
      deliverableType: $('select[id="deliverableType"]').val(),
      }, function(data) {
        location.reload();
        });
    return false;
}


$(function(){
  $('.datepicker').datepicker({
    format: 'mm-dd-yyyy'
  });
  $('#date').datepicker().on('changeDate', function(ev){
    $('#date').val(ev.target.value);
    });
});


function clearform(target){
$(target)
  .find("input[type=text],textarea,select")
    .val('')
    .end()
  .find("input[type=checkbox], input[type=radio]")
  .prop("checked", "")
  .end();
}

