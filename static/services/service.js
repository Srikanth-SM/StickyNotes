

app.service("getNotesService",['$http',function($http){
  var notes={};
  this.setNotes=function(data){
    notes=data;
  };
  this.getNotes=function(){
    return notes;
  };
}]);
