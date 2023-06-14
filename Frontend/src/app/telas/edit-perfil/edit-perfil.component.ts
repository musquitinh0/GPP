import { Component } from '@angular/core';
import { AccountService } from 'src/app/account/shared/account.service';

@Component({
  selector: 'app-edit-perfil',
  templateUrl: './edit-perfil.component.html',
  styleUrls: ['./edit-perfil.component.css']
})
export class EditPerfilComponent {
  user = {
    full_name: '',
    password: '',
    address: '',
  };
  
  constructor(
    private accountService: AccountService
  ) { }

  async onSubmit() {
    try {
      const result = await this.accountService.createAccount(this.user);

      //mensagem aqui de sucesso
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  }

}
