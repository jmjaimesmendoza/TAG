import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Socket } from 'ngx-socket-io';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  constructor (private fb: FormBuilder, private http: HttpClient, private socket: Socket, private toastr: ToastrService) {}

  showSuccess() {
    this.toastr.success('Websocket connected!');
  }

  title = 'application';
  loginForm!: FormGroup;
  displayedName: string = '';
  displayedSource: string = '';
  socketIsConnected: boolean = false;
  
  ngOnInit(){
    this.toastr.warning('Trying to reach WebSocket','', {"timeOut": 0})
    
    this.socket.on('connect', () => {
      this.socketIsConnected = true;
      this.toastr.clear();
      this.showSuccess();
    })

    this.socket.on('disconnect', () => {
      this.socketIsConnected = false;
      this.toastr.error('Lost connection to WebSocket')
    })
    
    this.socket.on('wsresponse',(data: any)=> {
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
      this.http.post('http://localhost:5420/submit', formData).subscribe((res:any) => {
        console.log(res);
      });
    }
  }
}
