#include <stdio.h>

// 定义一个表示星期几的枚举类型
typedef enum {
    MONDAY,     // 0
    TUESDAY,    // 1
    WEDNESDAY,  // 2
    THURSDAY,   // 3
    FRIDAY,     // 4
    SATURDAY,   // 5
    SUNDAY      // 6
} Weekday;

const char* get_weekday_name(Weekday day) {
    switch(day) {
        case MONDAY:    return "Monday";
        case TUESDAY:   return "Tuesday";
        case WEDNESDAY: return "Wednesday";
        case THURSDAY:  return "Thursday";
        case FRIDAY:    return "Friday";
        case SATURDAY:  return "Saturday";
        case SUNDAY:    return "Sunday";
        default:        return "Unknown";
    }
}

int main() {
    // 遍历枚举值并打印对应的名称
    // for (Weekday day = MONDAY; day <= SUNDAY; day++) {
    //     printf("%d: %s\n", day, get_weekday_name(day));
    // }
    for (int day = 0; day < 10; day++){
        printf("%d: %s\n", day, get_weekday_name(day));
    }
    return 0;
}
