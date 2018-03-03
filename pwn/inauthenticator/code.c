char* username[] = “admin”;
char* password[] = “password”;

int authenticate(char* provided_username, char* provided_password) {
	if (memcmp(username, provided_username, strlen(provided_username)) == 0 && memcmp(password, provided_password,strlen(provided_password)) == 0 ) {
	return 1;
  }
  else {
	  return 0;
  }
}

int main(int argc, char* argv[]) {
	return authenticate(argv[0], argv[1]);
}
