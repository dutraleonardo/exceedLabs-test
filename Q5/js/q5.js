/*
To run this script, you need to follow this steps:
1)Install a web server on your browser (Ex: 200 Ok for Chrome)
2)This script only works for users present in the "sandbox" the developer's api (me). 
The reason is because I could not turn on the "GO LIVE" button on api. (I'm really disappointed about this)  =(
3)Then to run the script, send me your username and I'll add you in the "sandbox". =)
*/
var urlPath = window.location.href;
console.log('URL: ' + urlPath);
var token = urlPath.substr(urlPath.indexOf('=')+1);
console.log('Token: ' + token);
$.ajax({
	type: 'GET',
	dataType: 'jsonp',
	url: 'https://api.instagram.com/v1/users/self/?access_token='+token,
	success: function(data){
		var infos = data.data;
		var fullName = infos.full_name;
		var followers = infos.counts.followed_by;
		var follows = infos.counts.follows;
		var picture = infos.profile_picture;
		console.log('Full Name: ' + infos.full_name);
		console.log('Followers: ' + infos.counts.followed_by);
		console.log('Following: ' + infos.counts.follows);
		
		$('.userInfo').append(
			"<img src='" + picture + "'>"
			+"<p><strong>User's Full Name:</strong> " + fullName + "</p>"
			+ "<p><strong>Followers:</strong> " + followers + "</p>"
			+ "<p><strong>Following:</strong> " + follows + "</p>"
		);
	}
	
})