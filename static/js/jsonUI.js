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
		  var resourceRow = "<ul class='inline'><li id='" + f.id + "'>" + f.name + "</li><li id='" + f.id + "'>" + f.cost + "</li></ul>";
		  $(resourceRow).appendTo("#resource");
		});
		updateSelectList($("#selRes"), data.resources)

	}
	//creates a tree call
	if('children' in data){
		$(tree(data.children)).appendTo("#task");
		updateSelectList($("#selChild"), data.children)
    	updateSelectList($("#selPred"), data.children)
    	updateSelectList($("#selSucc"), data.children)
    	updateSelectList($("#allocTask"), data.children)
    
	}
	
});

//creates a tree function
function tree(data){
	var str = "<ul>";
	$.each(data, function(i, f) {
		
		if(typeof(f.children) != 'undefined' ){
			str += "<li><span id='" + f.id + "' style='cursor:pointer' ><img class='arrow' src='static/rArrow.jpg'/>" + f.name + "</span>";
			str += tree(f.children) ;
		}
		else{
			str += "<li style='margin-left:20px'><span id='" + f.id + "' style='cursor:pointer'>" + f.name + "</span>";
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
	   		$('form[id="taskForm"]').attr("onsubmit", "return editTask()");
   			$('input[name="submitTask"]').val("Edit Task");
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
		alert(objectId);
		$.getJSON('static/data/Project.json', function(data) {
			editT(data.children, objectId); 
    	});
		console.log(task);
		
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
		$.getJSON('static/data/Project.json', function(data) {
			var resources = data.resources.filter(function(val, index, array) {
    			return val.id === objectId; 
    		});
   			$('input[name="resourceName"]').val(resources[0].name);
      		$('input[name="dailycost"]').val(resources[0].cost);
      		$('select[id="resourceType"]').val(resources[0].type);
      		$('select[id="allocTask"]').val(resources[0].allocTasks);
      		$('input[id="idHidden"]').val(objectId);
      		$('form[id="resourceForm"]').attr("onsubmit", "return editResource()");
       		$('input[name="submitResource"]').val("Edit Resource");

      	});
	});
});

//unselect if clicked outside of elements
$(document).click(function (e) {
	objectId = 0;
	$("span").removeClass("highlight");
	$("ul").removeClass("highlight");
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
    $.each(data, function(i, f) {
        var option = "<option value='"+f.id+"'>"+f.name+"</option>";
        $(option).appendTo(list)
    });
}
