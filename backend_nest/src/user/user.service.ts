import { Injectable, InternalServerErrorException } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';
import { PrismaService } from 'src/prisma/prisma.service';

@Injectable()
export class UserService {
  constructor(private readonly prisma: PrismaService) {}

  async createUser(createUserDto: CreateUserDto) {
    return this.prisma.user.create({data: createUserDto
    });
  }

//   async createUser(data: { name: string; email: string }) {
//     return this.prisma.user.create({ data }); // Crea un nuevo usuario
//   }
// }

  // async createUser(createUserDto: CreateUserDto) {
  //   try {
  //     return await this.prisma.user.create({
  //       data: createUserDto,
  //     });
  //   } catch (error) {
  //     throw new InternalServerErrorException("Error al crear el usuario");
  //   }
  // }

  async findAll() {
    return await this.prisma.user.findMany();
  }

  findOne(id: number) {
    return `This action returns a #${id} user`;
  }

  update(id: number, updateUserDto: UpdateUserDto) {
    return `This action updates a #${id} user`;
  }

  remove(id: number) {
    return `This action removes a #${id} user`;
  }
}
