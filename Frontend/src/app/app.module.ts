import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './account/login/login.component';
import { CreateAccountComponent } from './account/create-account/create-account.component';
import { HomeComponent } from './layout/home/home.component';
import { AuthenticationComponent } from './layout/authentication/authentication.component';
import { HttpClientModule } from '@angular/common/http';
import { HomeScreenComponent } from './telas/home-screen/home-screen.component';
import { PerfilComponent } from './telas/perfil/perfil.component';
import { httpInterceptorProviders } from './http-interceptors';
import { EditPerfilComponent } from './telas/edit-perfil/edit-perfil.component';
import { AddDispositivoComponent } from './telas/add-dispositivo/add-dispositivo.component';
import { PoliciaComponent } from './telas/policia/policia.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    CreateAccountComponent,
    HomeComponent,
    AuthenticationComponent,
    HomeScreenComponent,
    PerfilComponent,
    EditPerfilComponent,
    AddDispositivoComponent,
    PoliciaComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule,
  ],
  providers: [httpInterceptorProviders],
  bootstrap: [AppComponent]
})
export class AppModule { }
