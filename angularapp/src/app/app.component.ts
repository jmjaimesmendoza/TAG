import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Socket } from 'ngx-socket-io';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  constructor (private fb: FormBuilder, private http: HttpClient, private socket: Socket) {}
  title = 'application';
  loginForm!: FormGroup;
  displayedName: string = '';
  displayedSource: string = '';
  
  ngOnInit(){
    this.socket.on('eskeler',(data: any)=> {
      this.displayedName = data.name;
      this.displayedSource = data.source;
    })

    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    })
  }

  async onSubmit() {
    if (this.loginForm.valid) {
      const formData = this.loginForm.value
      this.http.post('http://localhost:5000/submit', formData).subscribe((res:any) => {
        console.log(res);
      });
    }
  }
}
