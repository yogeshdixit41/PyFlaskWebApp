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


function createTask(){
  if (!addTask()){
    $('#addTask').modal('hide');
  }
  return false;
}

function createResource(){
  if (!addResource()){
    $('#addResources').modal('hide');
  }
  return false;
}


function newProject() {
    $.getJSON('/project/newProject', {
      pname: $('input[name="pName"]').val(),
      date: $('input[name="date"]').val()
      }, function(data) {
        $('input[name="pName"]').val('')
        $('input[name="date"]').val('')
        $('div[name ="projectFrame"]').removeAttr("class")
        $("#projectName").append(data.name);
        console.log(data);
        //alert(data);
        });
    return false;
}

function addTask() {
    $.getJSON('/task/addTask', {
      taskName: $('input[name="taskName"]').val(),
      duration: $('input[name="duration"]').val(),
      optTaskType: $('input[name="optTaskType"]:checked').val(),
      selChild: $('input[id="selChild"]').val(),
      selPred: $('input[id="selPred"]').val(),
      selSucc: $('input[id="selSucc"]').val(),
      selRes: $('input[id="selRes"]').val(),
      taskDescription: $('textarea[name="taskDescription"]').val()
      }, function(data) {
        console.log(data);
        //alert(data);
        });
    return false;
}

function addResource() {
    $.getJSON('/resource/addResource', {
      resourceName: $('input[name="resourceName"]').val(),
      dailycost: $('input[name="dailycost"]').val(),
      resourceType: $('select[id="resourceType"]').val(),
      allocTask: $('select[name="allocTask"]').val()
      }, function(data) {
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
        console.log(data);
        //alert(data);
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

$('[data-dismiss=modal]').on('click', function (e) {
  var $t = $(this),
  target = $t[0].href || $t.data("target") || $t.parents('.modal') || [];
  clearform(target)
  
})

function clearform(target){
$(target)
  .find("input[type=text],textarea,select")
    .val('')
    .end()
  .find("input[type=checkbox], input[type=radio]")
  .prop("checked", "")
  .end();
}

