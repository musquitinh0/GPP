import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Profile } from './Profile';

@Injectable({
  providedIn: 'root'
})
export class PerfilService {

  constructor(private http: HttpClient) { }

  LoadProfile() {
    return this.http.get<Profile>(`${environment.api}/profile`);
  }

  mark_lost(phone: any){
    return this.http.post<any>(`${environment.api}/phone/lost`, {number: phone});
  }

}
