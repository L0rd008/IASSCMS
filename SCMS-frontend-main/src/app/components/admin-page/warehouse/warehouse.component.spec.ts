import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { WarehouseComponent } from './warehouse.component';

describe('WarehouseComponent', () => {
  let component: WarehouseComponent;
  let fixture: ComponentFixture<WarehouseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [WarehouseComponent, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WarehouseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});