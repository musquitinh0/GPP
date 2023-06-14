import { AccountService } from './account.service';
import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class authPoliciaGuard  implements CanActivate {

  constructor(
    private router: Router,
    private accountService: AccountService
  ) {}

  canActivate(next: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (this.accountService.isUserPolice()) {
      return true;
    } else {
      return false;
    }
  }
}
