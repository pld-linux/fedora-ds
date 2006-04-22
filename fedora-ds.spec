#
# http://directory.fedora.redhat.com/wiki/Building
#
Summary:	Fedora Directory Server
Summary(pl):	Fedora Directory Server - serwer us³ug katalogowych
Name:		fedora-ds
Version:	1.0.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	d8bd5b68087229b4bb2e3867cb92ba85
Patch0:		%{name}-make.patch
URL:		http://directory.fedora.redhat.com/
BuildRequires:	apr-devel
BuildRequires:	db-devel >= 4.0
BuildRequires:	libtermcap-devel
BuildRequires:	ncurses-devel
BuildRequires:	nspr-devel
BuildRequires:	rpmbuild(macros) >= 1.228
#BuildRequires:	java
#BuildRequires:	ant >= 1.6.1
#BuildRequires:	krb-devel
#BuildRequires:	httpd-devel
Requires:	libicu >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fedora Directory Server is a robust, scalable open-source server
designed to manage large directories of users and resources. It is
based on an open-systems server protocol called the Lightweight
Directory Access Protocol (LDAP). The Fedora Directory Server is a
world-class Directory Server implementation. Some of the more
interesting features that are included are:
- 4-Way Multi-Master Replication
- Scalability: thousands of operations per second, tens of thousands
  of concurrent users, tens of millions of entries, hundreds of
  gigabytes of data
- SSLv3, TLSv1, and SASL for secure authentication and transport
- Support for most LDAPv3 features, including many common controls and
  extensions
- Schema update over LDAP
- Flexible in-tree Access Control Information (ACIs), updatable over
  LDAP
- On-line configuration and management over LDAP
- Graphical console for all facets of user, group, and server
  management

%description -l pl
Fedora Directory Server to potê¿ny, posiadaj±cy otwarte ¼ród³a,
skalowalny serwer zaprojektowany do zarz±dzania du¿ymi katalogami
u¿ytkowników i zasobów. Jest oparty na otwartym protokole serwerowym
LDAP (Lightweight Directory Access Protocol). Fedora Directory Server
to ¶wiatowej klasy implementacja serwera us³ug katalogowych. Bardziej
interesuj±ce cechy obejmuj±:
- 4-stronn± replikacjê multi-master
- skalowalno¶æ: tysi±ce operacji na sekund±, dziesi±tki tysiêcy
  jednoczesnych u¿ytkowników, dziesi±tki milionów wpisów, setki
  gigabajtów danych
- obs³ugê SSLv3, TLSv1 i SASL do bezpiecznego uwierzytelniania i
  przesy³ania danych
- obs³ugê wiêkszo¶ci cech LDAPv3, w tym wielu popularnych opcji i
  rozszerzeñ
- uaktualnianie schematu przez LDAP
- elastyczne informacje o prawach dostêpu w drzewie (ACI - Access
  Control Information), uaktualniane przez LDAP
- konfiguracjê i zarz±dzanie w locie przez LDAP
- graficzn± konsolê dla wszystkich aspektów zarz±dzania u¿ytkownikami,
  grupami i serwerem

%prep
%setup -q
%patch0 -p1

%build
#%%configure
%{__make} -I/usr/include/nspr/

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}

#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

#%{_examplesdir}/%{name}-%{version}
