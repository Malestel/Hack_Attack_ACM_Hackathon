import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ClipboardModule } from '@angular/cdk/clipboard';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatFormFieldModule } from '@angular/material/form-field';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { ClientInfoComponent } from './client-info/client-info.component';
import { HomeComponent } from './home/home.component';
import { ChatComponent } from './chat/chat.component';
import { PreVideoComponent } from './pre-video/pre-video.component';
import { NavbarComponent } from './navbar/navbar.component';
import { CallinfoDialogComponent } from './callinfo-dialog/callinfo-dialog.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ClientInfoComponent,
    HomeComponent,
    ChatComponent,
    PreVideoComponent,
    NavbarComponent,
    CallinfoDialogComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    ClipboardModule,
    MatDialogModule,
    MatSnackBarModule,
    MatFormFieldModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
