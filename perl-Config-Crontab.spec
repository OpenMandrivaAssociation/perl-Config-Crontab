%define upstream_name    Config-Crontab
%define upstream_version 1.40


Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Read/Write Vixie compatible crontab(5) files 
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SC/SCOTTW/Config-Crontab-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Simple Time and Date module for perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.330.0-1mdv2011.0
+ Revision: 653986
- update to new version 1.33

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 408911
- rebuild using %%perl_convert_version

* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2009.1
+ Revision: 297811
- update to new version 1.30

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.21-3mdv2009.0
+ Revision: 256044
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.21-1mdv2008.1
+ Revision: 136690
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2008.0
+ Revision: 55685
- update to new version 1.21


* Wed Apr 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.20-1mdk
- New release 1.20

* Mon Dec 19 2005 Sebastien Savarin <plouf@mandriva.org> 1.11-1mdk
- First Mandriva package


