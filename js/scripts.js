/*!
* Start Bootstrap - Blog Home v5.0.8 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
function storeUserType(x){
    sessionStorage.setItem("usertype:", x);
    console.log(x);
    console.log(sessionStorage.getItem("usertype"));
}

document.getElementById('clickClient').addEventListener('change', storeUserType("client"), false);
document.getElementById('clickVolunteer').addEventListener('change', storeUserType("volunteer"), false);
