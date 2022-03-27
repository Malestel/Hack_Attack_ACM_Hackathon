/*import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  private url = environment.api_url;

  constructor(
    private httpClient: HttpClient
  ) { }

  getStuff(){
    this.httpClient.get(this.url  + '/api/user').subscribe({
      next: response => {
        console.log(response)
      }
    })
  }

  onLogin(phoneNumber: string){
    this.httpClient.post(this.url + '/login', {
      Phone_Number: phoneNumber
    }).subscribe({
      next: response => {
        console.log(response)
      }
    })
  }

  ngOnInit(): void {
  }

}*/

import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { environment } from 'src/environments/environment';
import { FormGroup, FormControl } from '@angular/forms';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router'; // CLI imports router
import {Router} from '@angular/router';




@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  profileForm = new FormGroup({
    phonenumber: new FormControl(''),
    lastName: new FormControl(''),
  });

  

  private url = environment.api_url;

  phoneNum: string = '';
  name: string = '';
  userType: string = '';
  language: string = '';

  constructor(
    private httpClient: HttpClient, private router:Router
  ) { }

  getStuff(){
    this.httpClient.get(this.url  + '/api/user').subscribe({
      //if 404 error, then get the user from the database

      next: response => {
        console.log(response)
        
      }
    })
  }

  onLogin(){
    this.httpClient.post<{
      Phone_Number: string,
      Name: string,
      user_type: string,
      Language: string
    }>(this.url + '/login', {
      Phone_Number: this.profileForm.value.phonenumber
    }).subscribe({
      next: (response) => {
        this.userType = response['user_type'];
        console.log( this.userType )
        if(this.userType == 'Users'){
          console.log('user');
          this.router.navigate(['/pre-vid']);
          //return  .redirect('/UserHomePage');
        }
        else if(this.userType == 'Volunteers'){
          console.log('volunteer');
          this.router.navigate(['/pre-vid']);
        }
        else{
          console.log('error')
        }
      }
    })
  }

  ngOnInit(): void {
  }
}

