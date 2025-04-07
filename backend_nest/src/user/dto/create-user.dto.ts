import { IsString } from 'class-validator';
import { } from 'class-transformer';

export class CreateUserDto {
  @IsString()
  name: string;
  @IsString()
  email: string;
}
