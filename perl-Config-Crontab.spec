%define      name       perl-%{realname}
%define      realname   Config-Crontab
%define      version    1.21
%define      release    %mkrel 1
%define      summary    TimeDate module for perl (Data_Type_Utilities/Time)


Name:           %name
Version:        %version
Release:        %release
License:        GPL
Summary:        %summary
Group:	        Development/Perl
Source0:        http://search.cpan.org/CPAN/authors/id/S/SC/SCOTTW/Config-Crontab-%{version}.tar.bz2
Url:	        http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch:      noarch

%description
Simple Time and Date module for perl.


%prep
%setup -q -n Config-Crontab-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

