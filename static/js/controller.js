app.controller("addNotesToDatabase", function($scope, $http, $location, getNotesService) {
    console.log("Inside Controller");
    // console.log(hai.h());
    // $scope.title="";
    // $scope.description="";
    // $scope.priority="";
    // $scope.noteList=[];
    // var s="";
    // $scope.dummy="";
    // this.noteList="";
    // $scope.noteList=[];
    $scope.viewNotes = function() {
        $scope.d = "";


        // console.log("inside view Notes");
        $http({
            method: 'GET',
            url: '/viewNotes',

        }).then(function(success) {
            console.log("Inside viewNotes");
            $scope.dummy = "sachin"
            console.log("inside viewNotes success");
            console.log("success= " + success);
            // var s=success.data.notesList;
            getNotesService.setNotes(success.data.notesList);
            // var length=success.data.notesList;
            // for (var i=0;i<length;i++){
            //   $scope.noteList.push(success.data.notesList[i]);
            // }
            // if($location.path()!="/viewNotes")
            // $location.path('/viewNotes');
            // $scope.noteList=success.data.notesList;
            // console.log("noteList "+$scope.noteList);
            $location.path('/viewNotes');
            console.log("sdsjd");

        })
        // $scope.noteList=s;
        console.log($scope.noteList);
    };
    // $scope.viewNotes();

    $scope.addInfo = function(info) {
        // console.log("hai " + info);
        console.log(info.title);
        $http({
            method: 'POST',
            url: '/addNotes',
            data: {
                'title': info.title,
                'description': info.description,
                'priority': info.priority
            }
        }).then(function(success) {
            console.log("sdadasdasd" + success);
            $scope.status = success.status;
            $scope.text = success.statusText;
            // $scope.headers = response.headers();
            if (success) {
                $scope.viewNotes();
                // $location.path('/viewNotes');

            } else {
                console.log(Error("Inside add INfo error"));
            }
        })
        //     }

    }


});




app.controller("getNotesFromDatabase", function($scope, $http, $location, getNotesService) {
    $scope.title = "sachin";
    $scope.noteList = getNotesService.getNotes();
    $scope.update = function(ele) {

        console.log("Inside update");
        console.log(ele.note);
        $http({
            method: 'POST',
            url: '/viewNotes',
             data:ele.note

        }).then(function(success) {
                if (success)
                    console.log("update success" + success);
                else {
                    console.log("update failed");
                }

            });
        };
});
