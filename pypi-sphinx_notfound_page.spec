#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinx_notfound_page
Version  : 0.8
Release  : 3
URL      : https://files.pythonhosted.org/packages/22/6f/15b7e282997c4a0e7273c8751dea84a673055624bae94a3c413e37284bbc/sphinx-notfound-page-0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/22/6f/15b7e282997c4a0e7273c8751dea84a673055624bae94a3c413e37284bbc/sphinx-notfound-page-0.8.tar.gz
Summary  : Sphinx extension to build a 404 page with absolute URLs
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx_notfound_page-license = %{version}-%{release}
Requires: pypi-sphinx_notfound_page-python = %{version}-%{release}
Requires: pypi-sphinx_notfound_page-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
|Build| |PyPI version| |Docs badge| |License|
sphinx-notfound-page
====================

%package license
Summary: license components for the pypi-sphinx_notfound_page package.
Group: Default

%description license
license components for the pypi-sphinx_notfound_page package.


%package python
Summary: python components for the pypi-sphinx_notfound_page package.
Group: Default
Requires: pypi-sphinx_notfound_page-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_notfound_page package.


%package python3
Summary: python3 components for the pypi-sphinx_notfound_page package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_notfound_page)

%description python3
python3 components for the pypi-sphinx_notfound_page package.


%prep
%setup -q -n sphinx-notfound-page-0.8
cd %{_builddir}/sphinx-notfound-page-0.8
pushd ..
cp -a sphinx-notfound-page-0.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656369958
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_notfound_page
cp %{_builddir}/sphinx-notfound-page-0.8/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_notfound_page/b99b217a3ed7d3106b05bf2587e781909c1595b3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_notfound_page/b99b217a3ed7d3106b05bf2587e781909c1595b3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
