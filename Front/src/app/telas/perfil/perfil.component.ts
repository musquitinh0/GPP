import { Component, OnInit } from '@angular/core';
import { PerfilService } from '../shared/perfil.service';
import { Profile } from '../shared/Profile';



@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent {

  profile: Profile = new Profile();

  constructor(private perfilService: PerfilService){};

  ngOnInit() {
    this.perfilService.LoadProfile().subscribe(profile => {
      this.profile = profile;
      console.log(this.profile);
    });
    
  }
  
  newPhone(){

  }

  marcarPerdido(phone: any){
    this.perfilService.mark_lost(phone).subscribe(Response => {
      console.log(Response);
    });
  }

}
