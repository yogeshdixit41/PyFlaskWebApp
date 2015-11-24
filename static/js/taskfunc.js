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
  req.open("GET", "https://secret-chamber-7094.herokuapp.com/naman", true);
  req.send();
  //req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  //req.send(form-encoded request body);
  return false;
}

/*
New Project Method
*/

function newProject() {
  //alert("Entered function..");
    $.getJSON('https://secret-chamber-7094.herokuapp.com/project/newProject', {
      pname: $('input[name="pName"]').val(),
      date: $('input[name="date"]').val()
      }, function(data) {
        console.log(data);
        //alert(data);
        });
    return false;
}

function addTask() {
    $.getJSON('https://secret-chamber-7094.herokuapp.com/task/addTask', {
      taskName: $('input[name="taskName"]').val(),
      duration: $('input[name="duration"]').val(),
      optTaskType: $('input[name="optTaskType"]').val(),
      selPred: $('input[name="selPred"]').val(),
      selSucc: $('input[name="selSucc"]').val(),
      selRes: $('input[name="selRes"]').val(),
      taskDescription: $('textarea[name="taskDescription"]').val()
      }, function(data) {
        console.log(data);
        //alert(data);
        });
    return false;
}

function addResource() {
    $.getJSON('https://secret-chamber-7094.herokuapp.com/resource/addResource', {
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
    $.getJSON('https://secret-chamber-7094.herokuapp.com/deliverable/addDeliverable', {
      deliverableName: $('input[name="deliverableName"]').val(),
      deliverableType: $('select[id="deliverableType"]').val(),
      }, function(data) {
        console.log(data);
        //alert(data);
        });
    return false;
}
