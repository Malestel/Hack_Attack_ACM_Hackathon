import { ComponentFixture, TestBed } from '@angular/core/testing';
import { PreVideoComponent } from './pre-video.component';
import {RouterTestingModule} from "@angular/router/testing";
import {AppComponent} from "../app.component";

describe('PreVideoComponent', () => {
  let component: PreVideoComponent;
  let fixture: ComponentFixture<PreVideoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PreVideoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PreVideoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});


