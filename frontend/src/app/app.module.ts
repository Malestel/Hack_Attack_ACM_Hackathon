import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { ClientInfoComponent } from './client-info/client-info.component';
import { ClipboardModule } from '@angular/cdk/clipboard'
import { HomeComponent } from './home/home.component';
import { ChatComponent } from './chat/chat.component';
import { PreVideoComponent } from './pre-video/pre-video.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MatTableModule } from '@angular/material/table';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatSnackBarModule } from '@angular/material/snack-bar'
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input'
import { CallinfoDialogComponent } from './callinfo-dialog/callinfo-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { CallService } from './call.service';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ClientInfoComponent,
    HomeComponent,
    ChatComponent,
    PreVideoComponent,
    NavbarComponent,
    CallinfoDialogComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    AppRoutingModule,
    MatTableModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatDialogModule,
    ClipboardModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatSnackBarModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    CallService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
