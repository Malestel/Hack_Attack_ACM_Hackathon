import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { DatePickerModule } from '@syncfusion/ej2-angular-calendars';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { ClientInfoComponent } from './client-info/client-info.component';
import { HomeComponent } from './home/home.component';
import { ChatComponent } from './chat/chat.component';
import { PreVideoComponent } from './pre-video/pre-video.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MatTableModule } from '@angular/material/table';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({

  declarations: [
    AppComponent,
    LoginComponent,
    ClientInfoComponent,
    HomeComponent,
    ChatComponent,
    PreVideoComponent,
    NavbarComponent,
  ],
  imports: [
    DatePickerModule,
    BrowserModule,
    FormsModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    AppRoutingModule,
    MatTableModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
