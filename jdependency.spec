%global pkg_name jdependency
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        0.7
Release:        10.11%{?dist}
Summary:        This project provides an API to analyse class dependencies
License:        ASL 2.0
URL:            http://github.com/tcurdt/%{pkg_name}
BuildArch:      noarch

Source0:        http://github.com/tcurdt/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz
# Upstream uses different version of objectweb-asm than Fedora has.
Patch0:         %{pkg_name}-asm.patch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}objectweb-asm
BuildRequires:  %{?scl_prefix_java_common}apache-commons-io

%description
%{pkg_name} is small library that helps you analyze class level
dependencies, clashes and missing classes.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%patch0
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 0.7-10.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0.7-10.10
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0.7-10.9
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 0.7-10.8
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0.7-10.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-10.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-10.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-10.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-10.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-10.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-10.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.7-10
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Jun 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-8
- Update to current packaging guidelines
- Fix test failures

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-7
- Remove unneeded BR: maven-idea-plugin

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.7-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7-3
- Fix date ordering in changelog
- Guidelines fixes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7-1
- Update to 0.7
- Fix BR to not require maven2
- Fix BR for new package name
- Adjust spec to new guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-3
- Add license to javadoc subpackage
- Change jakarta-commons-io for apache-commons-io
- Add BR to maven

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-2
- Rename from vafer-jdependency to jdependency alone

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-1
- Initial package
