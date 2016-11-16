Name:       libatomic_ops

%define keepstatic 1

Summary:    Atomic memory update operations
Version:    7.4.4
Release:    1
Group:      Development/Libraries
License:    GPL/MIT
URL:        http://www.hpl.hp.com/research/linux/atomic_ops/
Source0:    http://www.ivmaisoft.com/atomic_ops/download/%{name}-%{version}.tar.gz
BuildRequires:  coreutils

%description
Provides implementations for atomic memory update operations on a number of architectures. This allows direct use of these in reasonably portable code. Unlike earlier similar packages, this one explicitly considers memory barrier semantics, and allows the construction of code that involves minimum overhead across a variety of architectures

%package devel
Summary:    Atomic memory update operations
Group:      Development/Libraries

%description devel
Description: %{summary}


%prep
%setup -q -n %{name}-%{version}/upstream

chmod a-x AUTHORS ChangeLog COPYING README.md

%build

%autogen
%configure 
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%find_lang libatomic_ops || /bin/touch libatomic_ops.lang

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
fi
done


%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md
%{_includedir}/atomic_ops.h
%{_includedir}/atomic_ops_malloc.h
%{_includedir}/atomic_ops_stack.h
%{_includedir}/atomic_ops
%{_libdir}/%{name}*.a
%{_datadir}/%{name}
%{_libdir}/pkgconfig/*.pc
