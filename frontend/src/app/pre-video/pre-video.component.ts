import { Component, OnInit } from '@angular/core';
@Component({
  selector: 'app-pre-video',
  templateUrl: './pre-video.component.html',
  styleUrls: ['./pre-video.component.css']
})
export class PreVideoComponent implements OnInit {
  public minDate: Date = new Date ("05/07/2017");
  public maxDate: Date = new Date ("05/27/2017");
  public dateValue: Date = new Date ("05/16/2017");

  constructor() { }

  ngOnInit(): void {
  }

}
