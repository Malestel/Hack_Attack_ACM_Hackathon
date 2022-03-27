import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-client-info',
  templateUrl: './client-info.component.html',
  styleUrls: ['./client-info.component.css']
})
export class ClientInfoComponent implements OnInit {

  constructor() { }
  columnsToDisplay = ['userName', 'age'];


  ngOnInit(): void {
  }

}
function getStuff(this: any) {
  this.httpClient.get(this.url  + '/api/appointment').subscribe({
    next: (response: any) => {
      this.result = response;
      console.log(response)
    }
  })
}
