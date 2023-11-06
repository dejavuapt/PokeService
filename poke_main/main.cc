#include <drogon/drogon.h>
int main() {
    //Set HTTP listener address and port
    drogon::app().addListener("127.0.0.1", 5555);
    LOG_INFO << "Server running on 127.0.0.1";
    drogon::app().run();
    return 0;
}
