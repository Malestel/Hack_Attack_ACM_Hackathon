import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-client-info',
  templateUrl: './client-info.component.html',
  styleUrls: ['./client-info.component.css']
})
export class ClientInfoComponent implements OnInit {
  displayedColumns: string[] = ['table-name', 'table-phone', 'table-issue', 'demo-volunteer', 'demo-startT', 'demo-endT'];
  dataResult: any;
  constructor() { }
  ngOnInit(): void {
  }

}
function getStuff(this: any) {
  this.httpClient.get(this.url  + '/api/appointment').subscribe({
    next: (response: any) => {
      this.dataResult = response;
      console.log(response)
    }
  })
}
