#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-flink-shaded
Version  : 5.0
Release  : 2
URL      : https://github.com/apache/flink-shaded/archive/5.0.tar.gz
Source0  : https://github.com/apache/flink-shaded/archive/5.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/flink/flink-shaded-asm/5.0.4-6.0/flink-shaded-asm-5.0.4-6.0.jar
Source2  : https://repo1.maven.org/maven2/org/apache/flink/flink-shaded-asm/5.0.4-6.0/flink-shaded-asm-5.0.4-6.0.pom
Source3  : https://repo1.maven.org/maven2/org/apache/flink/flink-shaded-guava/18.0-6.0/flink-shaded-guava-18.0-6.0.jar
Source4  : https://repo1.maven.org/maven2/org/apache/flink/flink-shaded-guava/18.0-6.0/flink-shaded-guava-18.0-6.0.pom
Source5  : https://repo1.maven.org/maven2/org/apache/flink/flink-shaded-jackson/2.7.9-6.0/flink-shaded-jackson-2.7.9-6.0.jar
Source6  : https://repo1.maven.org/maven2/org/apache/flink/flink-shaded-jackson/2.7.9-6.0/flink-shaded-jackson-2.7.9-6.0.pom
Source7  : https://repo1.maven.org/maven2/org/apache/flink/flink-shaded/6.0/flink-shaded-6.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: mvn-flink-shaded-data = %{version}-%{release}
Requires: mvn-flink-shaded-license = %{version}-%{release}

%description
<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

%package data
Summary: data components for the mvn-flink-shaded package.
Group: Data

%description data
data components for the mvn-flink-shaded package.


%package license
Summary: license components for the mvn-flink-shaded package.
Group: Default

%description license
license components for the mvn-flink-shaded package.


%prep
%setup -q -n flink-shaded-5.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-flink-shaded
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-flink-shaded/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-flink-shaded/NOTICE
cp flink-shaded-asm-5/packaged_licenses/LICENSE.asm.txt %{buildroot}/usr/share/package-licenses/mvn-flink-shaded/flink-shaded-asm-5_packaged_licenses_LICENSE.asm.txt
cp flink-shaded-asm-6/packaged_licenses/LICENSE.asm.txt %{buildroot}/usr/share/package-licenses/mvn-flink-shaded/flink-shaded-asm-6_packaged_licenses_LICENSE.asm.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-asm/5.0.4-6.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-asm/5.0.4-6.0/flink-shaded-asm-5.0.4-6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-asm/5.0.4-6.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-asm/5.0.4-6.0/flink-shaded-asm-5.0.4-6.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-guava/18.0-6.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-guava/18.0-6.0/flink-shaded-guava-18.0-6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-guava/18.0-6.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-guava/18.0-6.0/flink-shaded-guava-18.0-6.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-jackson/2.7.9-6.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-jackson/2.7.9-6.0/flink-shaded-jackson-2.7.9-6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-jackson/2.7.9-6.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-jackson/2.7.9-6.0/flink-shaded-jackson-2.7.9-6.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded/6.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/flink/flink-shaded/6.0/flink-shaded-6.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-asm/5.0.4-6.0/flink-shaded-asm-5.0.4-6.0.jar
/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-asm/5.0.4-6.0/flink-shaded-asm-5.0.4-6.0.pom
/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-guava/18.0-6.0/flink-shaded-guava-18.0-6.0.jar
/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-guava/18.0-6.0/flink-shaded-guava-18.0-6.0.pom
/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-jackson/2.7.9-6.0/flink-shaded-jackson-2.7.9-6.0.jar
/usr/share/java/.m2/repository/org/apache/flink/flink-shaded-jackson/2.7.9-6.0/flink-shaded-jackson-2.7.9-6.0.pom
/usr/share/java/.m2/repository/org/apache/flink/flink-shaded/6.0/flink-shaded-6.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-flink-shaded/LICENSE
/usr/share/package-licenses/mvn-flink-shaded/NOTICE
/usr/share/package-licenses/mvn-flink-shaded/flink-shaded-asm-5_packaged_licenses_LICENSE.asm.txt
/usr/share/package-licenses/mvn-flink-shaded/flink-shaded-asm-6_packaged_licenses_LICENSE.asm.txt
