<<<<<<< HEAD

$.getJSON('/static/data/project.json', function(data) {
//gets the title
	$("#projectName").append(data.project);
//gets the schedule
   $.each(data.schedule, function(i, f) {
	  var tblRow = "<tr>" + "<td>" + f.date + "</td><td>";
		$.each(f.tasks, function(j, t) {
		  if( j == f.tasks.length-1){
		    tblRow +=  t;
		  }else{
		    tblRow +=  t + ", ";
		  }
		});
	  tblRow += "</td>" + "</tr>";
	   $(tblRow).appendTo("tbody");
    });
 //gets the resources
   $.each(data.resources, function(i, f) {
	  var resourceRow = "<ul class='inline'><li id='" + f.id + "'>" + f.resource + "</li><li id='" + f.id + "'>" + f.price + "</li></ul>";
	  $(resourceRow).appendTo("#resource");
    }); 
	//creates a tree call
	$(tree(data.tasks)).appendTo("#tasks");
});

//creates a tree function
function tree(data){
	var str = "<ul>";
	$.each(data, function(i, f) {
		
		if(typeof(f.children) != 'undefined' ){
			str += "<li><span id='" + f.id + "'><img class='arrow' src='/static/rArrow.jpg'/>" + f.label + "</span>";
			str += tree(f.children) ;
		}
		else{
			str += "<li style='margin-left:20px'><span id='" + f.id + "'>" + f.label + "</span>";
		}
		str += "</li>";
	})
	str += "</ul>";
	return str;
}
//selects the li span of a task
var objectId = 0;
$(function() {
	$("#tasks li span").on("click", function(e) {
		e.stopPropagation();
		objectId = this.id;
		alert(objectId);
		$("span").removeClass("highlight");
		$("ul").removeClass("highlight");
		$(this).addClass("highlight");
	});
});

//selects the ul of a resource
$(function() {
	$("#resource li").on("click", function(e) {
		e.stopPropagation();
		objectId = this.id;
		alert(objectId);
		$("span").removeClass("highlight");
		$("ul").removeClass("highlight");
		$(this).parent().addClass("highlight");
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
	//$("ul ul").hide();
	$("img").click(function(e){
		e.stopPropagation();
		$(this).parent().next("ul").toggle();

		var origsrc = $(this).attr('src');
        var src = '';
        if (origsrc == '/static/rArrow.jpg'){ src = '/static/dArrow.jpg';}
        else {src = '/static/rArrow.jpg'};
        $(this).attr('src', src);
	});
});

$('#ct').click(function(){
	$('#selChild').removeAttr("disabled");
	$('#duration').attr("value", "");
	$('#duration').attr("disabled","disabled");
});
$('#st').click(function(){
	$('#selChild').attr("disabled","disabled");
	$('#duration').removeAttr("disabled");
});

$('select[name*="task_list"]').change(function(){
	$('select[name*="task_list"] option').attr('disabled',false);
	$('select[name*="task_list"]').each(function(){
	    var $this = $(this);
	    $('select[name*="task_list"]').not($this).find('option').each(function(){
	       if($.inArray($(this).attr('value'),$this.val())>-1)
	           $(this).attr('disabled',true);
	    });
	 });
});

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
=======

$.getJSON('project.json', function(data) {
//gets the title
	$("#pName").append(data.project);
//gets the schedule
   $.each(data.schedule, function(i, f) {
	  var tblRow = "<tr>" + "<td>" + f.date + "</td><td>";
		$.each(f.tasks, function(j, t) {
		  if( j == f.tasks.length-1){
		    tblRow +=  t;
		  }else{
		    tblRow +=  t + ", ";
		  }
		});
	  tblRow += "</td>" + "</tr>";
	   $(tblRow).appendTo("tbody");
    });
 //gets the resources
   $.each(data.resources, function(i, f) {
	  var resourceRow = "<ul class='inline'><li id='" + f.id + "'>" + f.resource + "</li><li id='" + f.id + "'>" + f.price + "</li></ul>";
	  $(resourceRow).appendTo("#resource");
    }); 
	//creates a tree call
	$(tree(data.tasks)).appendTo("#task");
});

//creates a tree function
function tree(data){
	var str = "<ul>";
	$.each(data, function(i, f) {
		
		if(typeof(f.children) != 'undefined' ){
			str += "<li><span id='" + f.id + "'><img class='arrow' src='rArrow.jpg'/>" + f.label + "</span>";
			str += tree(f.children) ;
		}
		else{
			str += "<li style='margin-left:20px'><span id='" + f.id + "'>" + f.label + "</span>";
		}
		str += "</li>";
	})
	str += "</ul>";
	return str;
}
//selects the li span of a task
var objectId = 0;
$(function() {
	$("#task li span").on("click", function(e) {
		e.stopPropagation();
		objectId = this.id;
		alert(objectId);
		$("span").removeClass("highlight");
		$("ul").removeClass("highlight");
		$(this).addClass("highlight");
	});
});

//selects the ul of a resource
$(function() {
	$("#resource li").on("click", function(e) {
		e.stopPropagation();
		objectId = this.id;
		alert(objectId);
		$("span").removeClass("highlight");
		$("ul").removeClass("highlight");
		$(this).parent().addClass("highlight");
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
	$("ul ul").hide();
	$("img").click(function(e){
		e.stopPropagation();
		$(this).parent().next("ul").toggle();

		var origsrc = $(this).attr('src');
        var src = '';
        if (origsrc == 'rArrow.jpg'){ src = 'dArrow.jpg';}
        else {src = 'rArrow.jpg'};
        $(this).attr('src', src);
	});
});
>>>>>>> 9c3fda21d46de340bec3860c7ebd12809cc7709a
