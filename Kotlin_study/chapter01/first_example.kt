data class Person(
    val name: Stirng,
    val age: Int? = null
)

fun main(args: Array<Stirng>) {
    val persons = listOf(Person("영희"), Person("철수", age = 29))

    val oldest = persons.maxBy { it.age ?: 0}
    println("나이가 가장 많은 사람: $oldest")
}
