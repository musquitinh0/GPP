import { AccountService } from './../shared/account.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css']
})
export class CreateAccountComponent implements OnInit {
  user = {
    full_name: '',
    email: '',
    password: '',
    address: '',
    date_of_birth: '',
    cpf: ''
  };

  constructor(
    private accountService: AccountService
  ) { }

  ngOnInit() {
  }

  async onSubmit() {
    try {
      const result = await this.accountService.createAccount(this.user);
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  }
}
