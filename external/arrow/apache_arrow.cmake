include(ExternalProject)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

ExternalProject_Add(apache_arrow
        GIT_REPOSITORY "https://github.com/apache/arrow"
        GIT_TAG f10f5cfd1376fb0e602334588b3f3624d41dee7d
        PREFIX "${CMAKE_BINARY_DIR}/arrow/"
        INSTALL_DIR "${CMAKE_BINARY_DIR}/arrow/install"
        PATCH_COMMAND 
                sed "s| URL_HASH \"SHA256=.*\"||g" "./cpp/cmake_modules/ThirdpartyToolchain.cmake" > "./cpp/cmake_modules/ThirdpartyToolchain.cmake.new" 
                && mv "./cpp/cmake_modules/ThirdpartyToolchain.cmake.new" "./cpp/cmake_modules/ThirdpartyToolchain.cmake"
        CONFIGURE_COMMAND
        ${CMAKE_COMMAND} -G${CMAKE_GENERATOR} -DCMAKE_BUILD_TYPE=Release
        -DBUILD_WARNING_LEVEL=PRODUCTION -DARROW_DEPENDENCY_SOURCE=BUNDLED
        -DCMAKE_CXX_COMPILER_LAUNCHER=${CMAKE_CXX_COMPILER_LAUNCHER}
        -DCMAKE_CXX_FLAGS=${CMAKE_CXX_FLAGS}
        -DCMAKE_CXX_STANDARD=${CMAKE_CXX_STANDARD}
        -DCMAKE_C_COMPILER_LAUNCHER=${CMAKE_C_COMPILER_LAUNCHER}
        -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/arrow/install
        -DCMAKE_MODULE_PATH=${CMAKE_MODULE_PATH}
        -DCMAKE_TOOLCHAIN_FILE=${CMAKE_TOOLCHAIN_FILE} -DARROW_ALTIVEC=OFF
        -DARROW_USE_CCACHE=ON -DARROW_BOOST_USE_SHARED=OFF -DARROW_BUILD_SHARED=OFF
        -DARROW_BUILD_STATIC=ON -DARROW_COMPUTE=OFF -DARROW_CSV=ON -DARROW_IPC=ON -DARROW_JEMALLOC=OFF -DARROW_JSON=OFF
        -DARROW_PARQUET=ON -DARROW_SIMD_LEVEL=NONE -DARROW_RUNTIME_SIMD_LEVEL=NONE -DARROW_WITH_BROTLI=OFF
        -DARROW_WITH_LZ4=ON -Dlz4_SOURCE=BUNDLED -DARROW_WITH_PROTOBUF=OFF -DARROW_WITH_RAPIDJSON=OFF
        -DARROW_WITH_SNAPPY=ON -DSnappy_SOURCE=BUNDLED -DARROW_WITH_ZLIB=ON -DZLIB_SOURCE=BUNDLED
        -DARROW_WITH_ZSTD=ON -Dzstd_SOURCE=BUNDLED -DThrift_SOURCE=BUNDLED -DBOOST_SOURCE=BUNDLED -DARROW_WITH_RE2=OFF
        -DARROW_WITH_UTF8PROC=OFF -DARROW_BUILD_BENCHMARKS=OFF -DARROW_BUILD_EXAMPLES=OFF -DARROW_BUILD_INTEGRATION=OFF
        -DARROW_BUILD_UTILITIES=OFF -DARROW_BUILD_TESTS=OFF -DARROW_ENABLE_TIMING_TESTS=OFF -DARROW_FUZZING=OFF
        <SOURCE_DIR>/cpp
        UPDATE_COMMAND "")
