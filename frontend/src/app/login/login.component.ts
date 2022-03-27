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

  onLogin(){
    this.httpClient.post(this.url + '/login', {
      Phone_Number: this.profileForm.value.phonenumber
    }).subscribe({
      next: response => {
        console.log(response)
      }
    })
  }

  ngOnInit(): void {
  }
}

