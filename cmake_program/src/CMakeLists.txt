project(NuclF1F2)



# fill list of cpp files
set(NuclF1F2_SRCS ${NuclF1F2_SRCS}
NucleonStructure.cpp
mstwpdf.cpp
)


#fortran source files
set(NuclF1F2_FORT 
alekhin.f
F1F209_test.f
cteq.f
#spline.f
#clebsch.f
#getwavemod_tm.f
grsv2000pdf_g1.f
R199x.f
hmrs-b.f
)


#we dynamically configure the share directory in the constants.hpp file
set(SHARE_DIR "${CMAKE_SOURCE_DIR}/share")

configure_file (
  "${CMAKE_CURRENT_SOURCE_DIR}/constants.hpp.in"
  "${CMAKE_CURRENT_SOURCE_DIR}/constants.hpp"
  )


SET(NuclF1F2_SRCS_LI ${NuclF1F2_SRCS} ${NuclF1F2_FORT}) 

# Set the library version in the main CMakeLists.txt
SET(NuclF1F2_MAJOR_VERSION 1)
SET(NuclF1F2_MINOR_VERSION 0)
SET(NuclF1F2_PATCH_VERSION 0)
SET(NuclF1F2_VERSION "${NuclF1F2_MAJOR_VERSION}.${NuclF1F2_MINOR_VERSION}.${NuclF1F2_PATCH_VERSION}")
SET(NuclF1F2_LIBRARY_PROPERTIES ${NuclF1F2_LIBRARY_PROPERTIES}
    VERSION "${NuclF1F2_VERSION}"
    SOVERSION "${NuclF1F2_MAJOR_VERSION}"
    SUFFIX ".so"
    CLEAN_DIRECT_OUTPUT 1
)


############### build the library #####################
add_library(NuclF1F2 SHARED ${NuclF1F2_SRCS_LI})
target_include_directories(NuclF1F2 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_compile_options(NuclF1F2 PUBLIC "$<$<CONFIG:DEBUG>:${DEBUG_FLAGS}>")
target_compile_options(NuclF1F2 PUBLIC "$<$<CONFIG:RELEASE>:${RELEASE_FLAGS}>")
target_link_libraries(NuclF1F2)
set_target_properties(NuclF1F2 PROPERTIES ${NuclF1F2_LIBRARY_PROPERTIES})

############### install the library ###################
install(TARGETS NuclF1F2 DESTINATION "${CMAKE_SOURCE_DIR}/lib")

############# build the library #####################
if(STATIC_BUILD)
  add_library(NuclF1F2ST STATIC ${NuclF1F2_SRCS_LI})
  target_compile_options(NuclF1F2ST PUBLIC "$<$<CONFIG:DEBUG>:${DEBUG_FLAGS}>")
  target_compile_options(NuclF1F2ST PUBLIC "$<$<CONFIG:RELEASE>:${RELEASE_FLAGS}>")
  target_include_directories(NuclF1F2ST PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
  target_link_libraries(NuclF1F2ST -Wl,-no-whole-archive)
  set_target_properties(NuclF1F2ST PROPERTIES OUTPUT_NAME NuclF1F2)
  install(TARGETS NuclF1F2ST DESTINATION "${CMAKE_SOURCE_DIR}/lib")
endif(STATIC_BUILD)
