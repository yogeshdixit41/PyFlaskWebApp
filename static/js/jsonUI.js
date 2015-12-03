var schedule;

$.getJSON('static/data/Project.json', function(data) {
	//gets the title
	console.log(data)
	if('name' in data){
		$("#projectName").append(data.name);
	}
//gets the schedule
	if('schedule' in data){
		schedule = data.schedule;
	}
 //gets the resources
	if('resources' in data){
		$.each(data.resources, function(i, f) {
		  var resourceRow = "<ul class='inline'><li id='" + f.id + "'style='cursor:pointer'>" + f.name 
		  + "</li><li id='" + f.id + "cost'>" + f.cost + "</li></ul>";
		  $(resourceRow).appendTo("#resource");  
		  updateSelectList($("#selRes"), f)   
		});

	}
	//creates a tree call
	if('children' in data){
		$(tree(data.children)).appendTo("#task");
	}

	$('#dateSchedule').val(data.date);
	
});

//creates a tree function
function tree(data){
	var str = "<ul>";
	$.each(data, function(i, f) {
		updateSelectList($("#selChild"), f)
    	updateSelectList($("#selPred"), f)
    	updateSelectList($("#selSucc"), f)
    	updateSelectList($("#allocTask"), f)
	
		
		if(typeof(f.children) != 'undefined' ){
			str += "<li><span class='ttip' title='Description: " + f.desc + " " + getResources(f) + "'id='" + f.id + "' style='cursor:pointer' ><img class='arrow' src='static/rArrow.jpg'/>" + f.name + "</span>";
			str += tree(f.children) ;
		}
		else{
			str += "<li style='margin-left:20px'><span class='ttip' title='Description: " + f.desc + " " + getResources(f) + "'id='" + f.id + "' style='cursor:pointer'>" + f.name + "</span>";
		}
		str += "</li>";
	})
	str += "</ul>";
	return str;
}

function editT(data, id){
	$.each(data, function(i, f) {
		if (id == f.id) {
			$('input[name="taskName"]').val(f.name);
      		$('input[name="duration"]').val(f.duration);
   			$('textarea[name="taskDescription"]').val(f.desc);
  			$('input[id="idHidden"]').val(objectId);
  			$('select[id="selPred"]').val(f.pred);
  			$('select[id="selSucc"]').val(f.succ);
  			$('select[id="selRes"]').val(f.resources);
	   		$('form[id="taskForm"]').attr("onsubmit", "return editTask()");
   			$('input[name="submitTask"]').val("Edit Task");
   			if (f.children != 'undefined') {
   				$("#ct").attr('checked', 'checked');
   				$('select[id="selChild"]').val(f.children);
   			}
   			return false;
		}
		if(typeof(f.children) != 'undefined' ){
			editT(f.children, id);
		}
	});
}


//selects the li span of a task
var objectId = 0;
$(window).load(function() {
	$("#task li span").on("click", function(e) {
		e.stopPropagation();
		objectId = this.id;
		$("span").removeClass("highlight");
		$("ul").removeClass("highlight");
		$(this).addClass("highlight");
		$("a#editTask").removeClass("inactiveLink");  
		$("a#editResource").addClass("inactiveLink");
		$("#remove").attr("onclick", "return removeTask();");
		$.getJSON('static/data/Project.json', function(data) {
			editT(data.children, objectId); 
    	});
		//console.log(task);
		
    });
});

//selects the ul of a resource
$(window).load(function() {
	$("#resource li").on("click", function(e) {
		e.stopPropagation();
		objectId = this.id;
		$("span").removeClass("highlight");
		$("ul").removeClass("highlight");
		$(this).parent().addClass("highlight");
		$("a#editTask").addClass("inactiveLink");
		$("a#editResource").removeClass("inactiveLink");
		$("#remove").attr("onclick", "return removeResource();");
		$('input[id="idHidden"]').val(objectId);
		$.getJSON('static/data/Project.json', function(data) {
			var resources = data.resources.filter(function(val, index, array) {
    			return val.id === objectId; 
    		});
   			$('input[name="resourceName"]').val(resources[0].name);
      		$('input[name="dailycost"]').val(resources[0].cost);
      		$('select[id="resourceType"]').val(resources[0].type);
      		$('select[id="allocTask"]').val(resources[0].allocTasks);
      		
      		$('form[id="resourceForm"]').attr("onsubmit", "return editResource()");
       		$('input[name="submitResource"]').val("Edit Resource");

      	});
	});
});

// reset form if not Editing 
function resetResourceForm(){
	$('#resourceForm')[0].reset();
	$('form[id="resourceForm"]').attr("onsubmit", "return createResource()");
    $('input[name="submitResource"]').val("Create Resource");
    $('#idHidden').val('');
    return true;
}

function resetTaskForm(){
	$('#taskForm')[0].reset();
    $('form[id="taskForm"]').attr("onsubmit", "return createTask()");
   	$('input[name="submitTask"]').val("Create Task");
   	$('#idHidden').val('');
   	$("#st").attr('checked', 'checked');
   	return true;	
}

function getResources(task){
	var resourceNames = ["Resouces: "];
	$.each(task.resources, function (i, rId){
		resourceNames.push($('#'+rId).text());
	});
	return resourceNames.join(' ');
}
//unselect if clicked outside of elements
$(document).click(function (e) {
	objectId = 0;
	$("span").removeClass("highlight");
	$("ul").removeClass("highlight");
	$("a#editTask").addClass("inactiveLink");
	$("a#editResource").addClass("inactiveLink");
	$("#remove").removeAttr("onclick"); 	
});

//toggles the tree
$(function(){	
	$("#task ul ul").hide();
	$("img").click(function(e){
		e.stopPropagation();
		$(this).parent().next("ul").toggle();

		var origsrc = $(this).attr('src');
        var src = '';
        if (origsrc == 'static/rArrow.jpg'){ src = 'static/dArrow.jpg';}
        else {src = 'static/rArrow.jpg'};
        $(this).attr('src', src);
	});
});

//gets the current date
function getToday(){
	var date = new Date();
    var y = date.getFullYear().toString();
	var m = ("0" + (date.getMonth()+1)).slice(-2);
	var d = ("0" + date.getDate()).slice(-2);
	return (y + '-' + m + '-' + d);
}

//gets the calendar
$(document).ready(function() {
	$('#calendar').fullCalendar({
		defaultDate: getToday(),
		editable: false, // allows click and drag
		eventLimit: true, // allow "more" link when too many events
		events: schedule
	});
	
});

function updateSelectList(list, data){
    var option = "<option value='"+data.id+"'>"+data.name+"</option>";
    $(option).appendTo(list)
}

$(function(){
  $('.datepicker').datepicker({
    format: 'mm-dd-yyyy',
    autoclose: true
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
}

