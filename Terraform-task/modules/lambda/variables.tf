variable "runtime"{
  description = "Lambda function runtime"
  type=string
  default="python3.12"
}
variable "function_name"{
  type=string
  default="my_function"

}