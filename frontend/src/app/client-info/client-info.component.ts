import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-client-info',
  templateUrl: './client-info.component.html',
  styleUrls: ['./client-info.component.css']
})
export class ClientInfoComponent implements OnInit {
  private url = environment.api_url;

  displayedColumns: string[] = ['table-name', 'table-phone', 'table-issue', 'demo-volunteer', 'demo-startT', 'demo-endT'];
  dataResult: any;
  constructor(
    private httpClient: HttpClient
    ) {
    
   }
  ngOnInit(): void {
    this.getStuff();
  }
  getStuff(this: any) {
    this.httpClient.get(this.url  + '/api/appointment').subscribe({
      next: (response: any) => {
        this.dataResult = response;
        console.log(response)
      }
    })
  }
}