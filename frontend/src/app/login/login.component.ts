import { Component, OnInit } from '@angular/core';
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

  ngOnInit(): void {
  }

}
