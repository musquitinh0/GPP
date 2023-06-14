import { TestBed, async, inject } from '@angular/core/testing';

import { authPoliciaGuard } from './auth-policia.guard';

describe('AuthGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [authPoliciaGuard]
    });
  });

  it('should ...', inject([authPoliciaGuard], (guard: authPoliciaGuard) => {
    expect(guard).toBeTruthy();
  }));
});