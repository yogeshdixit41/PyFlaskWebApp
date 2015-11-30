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


/* XMLHttp request callback mechanism - Not used
// Create the callback:
var req = createRequest(); // defined above
req.onreadystatechange = function() {
  if (req.readyState != 4) return; // Not there yet
  if (req.status != 200) {
    // Handle request failure here...
    return;
  }
  // Request successful, read the response
  var resp = req.responseText;
  alert(resp);
  // ... and use it as needed by your app.
}
*/

/*
New Project method - XMLHttp request mechanism impl
*/

function newProject1() {
  req.open("GET", "/naman", true);
  req.send();
  //req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  //req.send(form-encoded request body);
  return false;
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

function newProject() {
<<<<<<< HEAD
    $.getJSON('/project/newProject', {
=======
    $.getJSON('/newProject', {
>>>>>>> 9c3fda21d46de340bec3860c7ebd12809cc7709a
      pname: $('input[name="pName"]').val(),
      date: $('input[name="date"]').val()
      }, function(data) {
        $('input[name="pName"]').
        console.log(data);
        //alert(data);
        });
    return false;
}

function addTask() {
    $.getJSON('/task/addTask', {
      taskName: $('input[name="taskName"]').val(),
      duration: $('input[name="duration"]').val(),
      optTaskType: $('input[name="optTaskType"]').val(),
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
      allocTask: $('input[name="allocTask"]').val()
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

