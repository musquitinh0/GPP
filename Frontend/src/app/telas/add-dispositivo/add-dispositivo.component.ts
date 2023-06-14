import { Component } from '@angular/core';
import { AccountService } from 'src/app/account/shared/account.service';

@Component({
  selector: 'app-add-dispositivo',
  templateUrl: './add-dispositivo.component.html',
  styleUrls: ['./add-dispositivo.component.css']
})
export class AddDispositivoComponent {
  phone = {
    modelo: '',
    number: '',
    imei: ''
  }
  constructor(
    private accountService: AccountService
  ) { }

  async onSubmit() {
    try {
      const result = await this.accountService.createAccount(this.phone);

      //mensagem aqui de sucesso
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  }
}
