output "public_subnet_id_1" {

    value = aws_subnet.public1.id
  
}


output "public_subnet_id_2" {

    value = aws_subnet.public2.id
  
}


output "private_subnet_id_1" {

    value = aws_subnet.private1.id
  
}


output "private_subnet_id_2" {

    value = aws_subnet.private2.id
  
}


output "myvpc" {
    value = aws_vpc.myvpc.id
  
}