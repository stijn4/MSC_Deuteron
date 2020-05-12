project(poldeut)

add_executable(structure_function structure_function.cpp )
target_link_libraries(structure_function NuclF1F2 )

install(TARGETS structure_function DESTINATION "${CMAKE_SOURCE_DIR}/bin")

